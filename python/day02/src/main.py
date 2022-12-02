def main():
    with open('../input.txt', 'r') as f: input = f.read()
    parsed_input = [line.split(' ') for line in input.split("\n")]
    print(f"Silver: {silver(parsed_input)}")
    print(f"Gold: {gold(parsed_input)}")

def silver(input):
    total = 0
    for game in input:
        if game[1] == 'X':
            total += 1
            if game[0] == 'C':
                total += 6
            elif game[0] == 'A':
                total += 3
        elif game[1] == 'Y':
            total += 2
            if game[0] == 'A':
                total += 6
            elif game[0] == 'B':
                total += 3
        elif game[1] == 'Z':
            total += 3
            if game[0] == 'B':
                total += 6
            elif game[0] == 'C':
                total += 3
    return total


def gold(input):
    total = 0
    for game in input:
        if game[1] == 'X':
            if game[0] == 'C':
                total += 2
            elif game[0] == 'A':
                total += 3
            else:
                total += 1
        elif game[1] == 'Y':
            total +=3
            if game[0] == 'A':
                total += 1
            elif game[0] == 'B':
                total += 2
            else:
                total += 3
        elif game[1] == 'Z':
            total += 6
            if game[0] == 'B':
                total += 3
            elif game[0] == 'C':
                total += 1
            else:
                total += 2
    return total

main()