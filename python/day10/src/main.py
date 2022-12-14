import itertools


def parse_input(plain_text):
    output = [] 
    for line in plain_text.strip().splitlines():
        output.append(0)
        if not line.strip() == 'noop':
            _, value = line.strip().split(' ')
            output.append(int(value))
    return output

def compute_register_state(instructions):
    return list(itertools.accumulate(instructions, initial=1))

def main():
    input_silver = [l.split() for l in open('../input.txt').readlines()]
    with open('../input.txt') as f:
        plain_text = f.read()
    input_gold = parse_input(plain_text)

    print(f'Silver: {silver(input_silver)}')
    print(f'Gold: {gold(input_gold)}')

def silver(input):
    signals = [x*40+20 for x in range(6)]
    output = 0
    register = 1
    cycles = 0
    for l in input:
        match l:
            case ['noop']: 
                cycles += 1
                if cycles in signals:
                    output += register * round(cycles/10)*10
            case ['addx', x]: 
                cycles += 2
                if cycles in signals or cycles-1 in signals:
                    output += register * round(cycles/10)*10
                register += int(x)
    return output

def gold(input):
    register = compute_register_state(input)
    display = [[0 for _ in range(40)] for _ in range(6)]

    for cycle in range(240):
        is_on = int(abs(register[cycle] - cycle % 40) <= 1)
        display[cycle // 40][cycle % 40] = is_on 

    return '\n'+'\n'.join([''.join([('.', '#')[i] for i in row]) for row in display])

if __name__ == '__main__':
    main()