with open('input.txt', 'r') as f: input = f.read().split('\n')

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

print(sum(max))