def main():
    input = [[int(row) for row in col.strip()] for col in open('../input.txt').readlines()]
    print(f'Silver: {silver(input)}')
    print(f'Gold: {gold(input)}')

def is_visible(input, y, xidx, yidx):
    same_col = [input[z][xidx] for z in range(len(input))]
    if all(input[yidx][xidx] > i for i in y[:xidx]) or \
        all(input[yidx][xidx] > i for i in y[xidx+1:]) or \
        all(input[yidx][xidx] > i for i in same_col[:yidx]) or \
        all(input[yidx][xidx] > i for i in same_col[yidx+1:]):
        return 1
    return 0

def unobstructed_view(val, l):
    total = 0
    for x in l:
        total += 1
        if val <= x:
            return total
    return total

def calc_score(input, y, xidx, yidx):
    same_col = [input[z][xidx] for z in range(len(input))]
    if xidx == 0 or xidx == len(input)-1 or yidx == 0 or yidx == len(same_col)-1:
        return 0
    left = unobstructed_view(input[yidx][xidx], y[:xidx][::-1])
    right = unobstructed_view(input[yidx][xidx], y[xidx+1:])
    up = unobstructed_view(input[yidx][xidx], same_col[:yidx][::-1])
    down = unobstructed_view(input[yidx][xidx], same_col[yidx+1:])
    return left * right * up * down

def silver(input):
    total = 0
    for yidx, y in enumerate(input):
        for xidx, _ in enumerate(y):
            total += is_visible(input, y, xidx, yidx)
    return total

def gold(input):
    max_score = 0
    for yidx, y in enumerate(input):
        for xidx, _ in enumerate(y):
            max_score = max(max_score, calc_score(input, y, xidx, yidx))
    return max_score

main()