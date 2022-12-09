from collections import namedtuple

Coord = namedtuple("Coord", "y x")

def is_touching(head, tail):
    return True if abs(head.y - tail.y) <= 1 and abs(head.x - tail.x) <= 1 else False

def get_next_tail(head, tail):
    if is_touching(head, tail): return tail
    if head.y == tail.y: return Coord(head.y, (head.x + tail.x) // 2)
    if head.x == tail.x: return Coord((head.y + tail.y) // 2, head.x)
    for i in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
        next_tail = Coord(tail.y + i[0], tail.x + i[1])
        if is_touching(next_tail, head): return next_tail

def traverse_grid(input):
    visited = [set() for _ in range(9)]
    head = Coord(0,0)
    tails = [Coord(0,0) for _ in range(9)]
    for direction, distance in input:
        for _ in range(int(distance)):
            match direction:
                case 'U': head = Coord(head.y + 1, head.x)
                case 'D': head = Coord(head.y - 1, head.x)
                case 'L': head = Coord(head.y, head.x - 1)
                case 'R': head = Coord(head.y, head.x + 1)
            tails[0] = get_next_tail(head, tails[0])
            for i in range(1, 9):
                tails[i] = get_next_tail(tails[i-1], tails[i])
            for i in range(9):
                visited[i].add(tails[i])
    return visited
    
def main():
    input = [l.split() for l in open('../input.txt').readlines()]
    visited = traverse_grid(input)
    print(f'Silver: {silver(visited)}')
    print(f'Gold: {gold(visited)}')

def silver(visited):
    return len(visited[0])

def gold(visited):
    return len(visited[8])

main()