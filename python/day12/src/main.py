from functools import total_ordering
from heapq import heappop, heappush


@total_ordering
class Node:
    def __init__(self, elevation: str):
        self.neighbors = []
        self.is_start = False 
        self.is_end = False 
        self.distance = 99999
        match elevation:
            case 'S':
                self.is_start = True 
                self.elevation = 'a' 
            case 'E':
                self.is_end = True 
                self.elevation = 'z'
            case _: 
                self.elevation = elevation

    def add_neighbor(self, other: 'Node'):
        if ord(self.elevation) - ord(other.elevation) >= -1:
            self.neighbors.append(other)

    def __lt__(self, other):
        return self.distance < other.distance

def reset(grid):
    for row in grid:
        for node in row:
            node.distance = 99999

def silver(grid):
    start_nodes = [node for row in grid for node in row if node.is_start]
    distances_to_end = []
    for start in start_nodes:
        reset(grid)
        start.distance = 0
        unvisited = [start]
        current = Node('xaa') 
        while not current.is_end:
            if len(unvisited) == 0: break
            current = heappop(unvisited)
            distance = current.distance + 1
            for v in current.neighbors:
                if distance < v.distance:
                    v.distance = distance 
                    heappush(unvisited, v)
        if current.is_end: distances_to_end.append(current.distance) 
    return min(distances_to_end)

def gold(grid):
    start_nodes = []
    for row in grid:
        for node in row:
            if node.elevation == 'a':
                start_nodes.append(node)
    distances_to_end = []
    for start in start_nodes:
        reset(grid)
        start.distance = 0
        unvisited = [start]
        current = Node('xaa') 
        while not current.is_end:
            if len(unvisited) == 0: break
            current = heappop(unvisited)
            distance = current.distance + 1
            for v in current.neighbors:
                if distance < v.distance:
                    v.distance = distance 
                    heappush(unvisited, v)
        if current.is_end: distances_to_end.append(current.distance) 
    return min(distances_to_end)

def main():
    grid = [[Node(x) for x in line.strip()] for line in open('../input.txt').readlines()]
    for row, _ in enumerate(grid):
        for col, node in enumerate(grid[row]):
            if row > 0: node.add_neighbor(grid[row-1][col])
            if col > 0: node.add_neighbor(grid[row][col-1])
            if row < len(grid) - 1: node.add_neighbor(grid[row+1][col])
            if col < len(grid[0]) - 1: node.add_neighbor(grid[row][col+1])

    print(f'Silver: {silver(grid)}')
    print(f'Gold: {gold(grid)}')

if __name__ == '__main__':
    main()