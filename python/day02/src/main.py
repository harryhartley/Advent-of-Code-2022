rps = {
    "A X": (4, 3), "A Y": (8, 4), "A Z": (3, 8),
    "B X": (1, 1), "B Y": (5, 5), "B Z": (9, 9),
    "C X": (7, 2), "C Y": (2, 6), "C Z": (6, 7),
}

def main():
    input = [l.strip() for l in open("../input.txt").readlines()]
    print(f"Silver: {silver(input)}")
    print(f"Gold: {gold(input)}")

def silver(input):
    return sum(rps[x][0] for x in input)

def gold(input):
    return sum(rps[x][1] for x in input)

main()