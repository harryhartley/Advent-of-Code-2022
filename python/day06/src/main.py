def main():
    input = [l for l in open('../input.txt').read().strip()]
    print(f'Silver: {silver(input)}')
    print(f'Gold: {gold(input)}')

def first_substring(input, length):
    buffer = []
    for idx, x in enumerate(input):
        if len(buffer) == length:
            return idx
        if x in buffer:
            buffer = buffer[buffer.index(x)+1:]
        buffer.append(x)
    return -1

def silver(input):
    return first_substring(input, 4)

def gold(input):
    return first_substring(input, 14)

main()