def main():
    input = [l.strip() for l in open("../input.txt").readlines()]
    print(f"Silver: {silver(input)}")
    print(f"Gold: {gold(input)}")

def silver(input):
    total = 0
    x = [l.split(',') for l in input]
    for y in x:
        a = y[0].split('-')
        b = y[1].split('-')
        if (int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]) or int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])):
            total += 1
    return total

def gold(input):
    total = 0
    x = [l.split(',') for l in input]
    for y in x:
        a = y[0].split('-')
        b = y[1].split('-')
        if not (int(a[0]) > int(b[1]) or int(a[1]) < int(b[0])):
            total += 1
    return total

main()