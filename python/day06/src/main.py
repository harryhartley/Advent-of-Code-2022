def main():
    input = [l for l in open('../input.txt').read().strip()]
    print(f'Silver: {silver(input)}')
    print(f'Gold: {gold(input)}')

def silver(input):
    buffer = []
    for idx, x in enumerate(input):
        if len(buffer) == 4:
            return idx
        if x in buffer:
            buffer = buffer[buffer.index(x)+1:]
        buffer.append(x)
    return -1

def gold(input):
    buffer = []
    for idx, x in enumerate(input):
        if len(buffer) == 14:
            return idx
        if x in buffer:
            buffer = buffer[buffer.index(x)+1:]
        buffer.append(x)
    return -1

main()