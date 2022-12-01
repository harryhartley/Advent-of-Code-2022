with open('input.txt', 'r') as f: input = f.read().split('\n')

max = 0
temp = 0

for x in input:
    if x == '':
        if temp > max:
            max = temp
        temp = 0
    else:
        temp += int(x)

print(max)