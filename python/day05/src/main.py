import re

def main():
    input = [l.strip("\n") for l in open("../input.txt").readlines()]
    crates = input[:8]
    state = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for x in crates:
        for idx, char in enumerate(x):
            if char.isupper():
                state[idx//4+1] = [char] + state[idx//4+1]
    print(state)
    instructions = input[10:]
    # print(f"Silver: {silver(state, instructions)}")
    print(f"Gold: {gold(state, instructions)}")

def silver(state, instructions):
    for i in instructions:
        instruction = re.split(' from | to ', i[5:])
        for _ in range(int(instruction[0])):
            temp = state[int(instruction[1])].pop()
            state[int(instruction[2])] += temp
    return state

def gold(state, instructions):
    for i in instructions:
        instruction = re.split(' from | to ', i[5:])
        temp = state[int(instruction[1])][-int(instruction[0]):]
        for _ in range(int(instruction[0])):
            state[int(instruction[1])].pop()
        state[int(instruction[2])] += temp
    return state

main()