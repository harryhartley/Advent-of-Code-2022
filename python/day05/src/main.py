import re
import copy

def get_last_chars(d):
    return ''.join([v[-1] for _, v in d.items()])

def main():
    input = [l.strip("\n") for l in open("../input.txt").readlines()]
    state = {i+1:[] for i in range(9)}
    for x in input[:8]:
        for idx, char in enumerate(x):
            if char.isupper():
                state[idx//4+1] = [char] + state[idx//4+1]
    print(f"Silver: {silver(copy.deepcopy(state), input[10:])}")
    print(f"Gold: {gold(state, input[10:])}")

def silver(state, instructions):
    for i in instructions:
        instruction = re.split(' from | to ', i[5:])
        for _ in range(int(instruction[0])):
            state[int(instruction[2])] += state[int(instruction[1])].pop()
    return get_last_chars(state)

def gold(state, instructions):
    for i in instructions:
        instruction = re.split(' from | to ', i[5:])
        state[int(instruction[2])] += state[int(instruction[1])][-int(instruction[0]):]
        for _ in range(int(instruction[0])):
            state[int(instruction[1])].pop()
    return get_last_chars(state)

main()