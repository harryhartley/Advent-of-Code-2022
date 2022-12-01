def main():
    with open('./input.txt', 'r') as f: input = f.read().split('\n')
    print(f"Silver: {silver(input)}")
    print(f"Gold: {gold(input)}")

def silver(input):
    max = 0
    temp = 0
    for x in input:
        if x == '':
            if temp > max:
                max = temp
            temp = 0
        else:
            temp += int(x)
    return max

def gold(input):
    max = []
    temp = 0
    for x in input:
        if x == '':
            if len(max) < 3:
                max.append(temp)
                max = sorted(max)
            else:
                if max[0] < temp:
                    max[0] = temp
                    max = sorted(max)
            temp = 0
        else:
            temp += int(x)
    return sum(max)

main()