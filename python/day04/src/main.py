def main():
    input = [[list(map(lambda z: int(z), y.split('-'))) for y in x.split(',')] for x in [l.strip() for l in open("../input.txt").readlines()]]
    print(f"Silver: {silver(input)}")
    print(f"Gold: {gold(input)}")

def silver(input):
    return sum(x[0][0] <= x[1][0] and x[0][1] >= x[1][1] or x[0][0] >= x[1][0] and x[0][1] <= x[1][1] for x in input)

def gold(input):
    return sum(x[0][0] <= x[1][1] and x[1][0] <= x[0][1] for x in input)

main()