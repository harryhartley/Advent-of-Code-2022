def main():
    input = [l for l in open('../input.txt').read().strip()]
    print(f'Silver: {silver(input)}')
    print(f'Gold: {gold(input)}')

def silver(input):
    buffer = []
    for idx, x in enumerate(input):
        if x not in buffer:
            buffer.append(x)
            if len(buffer) == 4:
                return idx + 1
        else: buffer = buffer[buffer.index(x)+1:] + [x]
    return -1

def gold(input):
    buffer = []
    for idx, x in enumerate(input):
        if x not in buffer:
            buffer.append(x)
            if len(buffer) == 14:
                return idx + 1
        else: buffer = buffer[buffer.index(x)+1:] + [x]
    return -1

main()