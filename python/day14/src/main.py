def main():
    board = set()
    input = [[tuple(map(lambda x: int(x), s.split(','))) \
        for s in line.strip().split(' -> ')] \
            for line in open('../input.txt').readlines()]
    for row in input:
        for (x, y),(i, j) in zip(row, row[1:]):
            board.update((a, y) for a in range(x, i+1))
            board.update((a, y) for a in range(i, x+1))
            board.update((x, b) for b in range(j, y+1))
            board.update((x, b) for b in range(y, j+1))
    H = max(p[1] for p in board)
    L = min(p[0] for p in board)
    R = max(p[0] for p in board)
    board.update((z, H+2) for z in range(L-H, R+H))

    print(f'Silver: {silver(board, H, R)}')
    print(f'Gold: {gold(board, H, R)}')

def silver(board, H, R):
    for c in range(H * R):
        sand = (500, 0)
        while sand not in board:
            match sand:
                case (a, b) if (a, b+1) not in board: sand = (a, b+1)
                case (a, b) if (a-1, b+1) not in board: sand = (a-1, b+1)
                case (a, b) if (a+1, b+1) not in board: sand = (a+1, b+1)
                case _: board.add(sand)
        if sand[1] >= H: 
            return c

def gold(board, H, R):
    for c in range(H * R):
        sand = (500,0)
        while sand not in board:
            match sand:
                case (a, b) if (a, b+1) not in board: sand = (a, b+1)
                case (a, b) if (a-1, b+1) not in board: sand = (a-1, b+1)
                case (a, b) if (a+1, b+1) not in board: sand = (a+1, b+1)
                case _: board.add(sand)
        if sand[1] >= H: H*=H
        if sand[1] == 0: return c+1

if __name__ == "__main__":
    main()