from collections import defaultdict


def main():
    input = [l.strip() for l in open('../input.txt').readlines()]
    sizes = defaultdict(int)
    stack = []
    for l in input[1:]:
        match l.split():
            case [_, _, ".."]: stack.pop()
            case [_, _, x]: stack.append(x)
            case [a, _] if a.isdigit():
                for i in range(len(stack) + 1):
                    path = "/" + "/".join(stack[:i])
                    sizes[path] += int(a)
    print(f'Silver: {silver(sizes)}')
    print(f'Gold: {gold(sizes)}')

def silver(sizes):
    return sum(filter(lambda v: v <= 100000, sizes.values()))

def gold(sizes):
    unused = 70000000 - sizes["/"]
    need = 30000000 - unused
    return min(filter(lambda v: v >= need, sizes.values()))

main()