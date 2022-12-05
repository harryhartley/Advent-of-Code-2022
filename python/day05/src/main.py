import re
import copy

def get_last_chars(d):
    return ''.join([v[-1] for _, v in d.items()])

def main():
    input = [l.strip('\n') for l in open('../input.txt').readlines()]
    state = {i+1:[] for i in range(9)}
    for x in input[:8]:
        for idx, char in enumerate(x):
            if char.isupper():
                state[idx//4+1] = [char] + state[idx//4+1]
    instructions = map(lambda i : re.split(' from | to ', i[5:]), input[10:])
    print(f'Silver: {silver(copy.deepcopy(state), instructions)}')
    print(f'Gold: {gold(state, instructions)}')

def silver(state, instructions):
    for instruction in instructions:
        for _ in range(int(instruction[0])):
            state[int(instruction[2])] += state[int(instruction[1])].pop()
    return get_last_chars(state)

def gold(state, instructions):
    for instruction in instructions:
        state[int(instruction[2])] += state[int(instruction[1])][-int(instruction[0]):]
        for _ in range(int(instruction[0])):
            state[int(instruction[1])].pop()
    return get_last_chars(state)

main()