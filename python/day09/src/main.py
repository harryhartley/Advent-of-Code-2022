def isTouching(head, tail):
    return True if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1 else False

def getNextTail(head, tail):
    if isTouching(head, tail): return tail
    if head[0] == tail[0]: return (head[0], (head[1] + tail[1])//2)
    if head[1] == tail[1]: return ((head[0] + tail[0])//2, head[1])
    for x in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
        possible = (tail[0] + x[0], tail[1] + x[1])
        if isTouching(possible, head): return possible

def traverse(input):
    visited = [set() for _ in range(9)]
    head = (0,0)
    tails = [(0,0) for _ in range(9)]
    for direction, distance in input:
        for _ in range(int(distance)):
            match direction:
                case 'U': head = (head[0] + 1, head[1])
                case 'D': head = (head[0] - 1, head[1])
                case 'L': head = (head[0], head[1] -1)
                case 'R': head = (head[0], head[1] + 1)
            tails[0] = getNextTail(head, tails[0])
            for i in range(1, 9):
                tails[i] = getNextTail(tails[i-1], tails[i])
            for i in range(9):
                visited[i].add(tails[i])
    return visited
    
def main():
    input = [l.split() for l in open('../input.txt').readlines()]
    visited = traverse(input)
    print(f'Silver: {silver(visited)}')
    print(f'Gold: {gold(visited)}')

def silver(visited):
    return len(visited[0])

def gold(visited):
    return len(visited[8])

main()