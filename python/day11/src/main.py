import copy
from math import prod


def increase_worry_level(monkey):
    item = monkey['items'][0]
    if monkey['sign'] == '*':
        mult = item
        if monkey['value'] != 'old':
            mult = int(monkey['value'])
        monkey['items'][0] *= mult
    else: monkey['items'][0] += int(monkey['value'])
 
def control_worry_level(monkey, mod=None):
    if mod is None: monkey['items'][0] //= 3
    else: monkey['items'][0] %= mod
 
def is_divisible(monkey):
    return monkey['items'][0] % monkey['div'] == 0
 
def move_item(monkey, monkeys, is_divisible):
    item = monkey['items'].pop(0)
    if is_divisible: target_monkey_index = monkey['true']
    else: target_monkey_index = monkey['false']
    monkeys[target_monkey_index]['items'].append(item)

def gen_monkey(monkey):
    return {
        'items': list(map(int, monkey[1].split(': ')[1].split(','))),
        'sign': monkey[2].split('old ')[1].split()[0],
        'value': monkey[2].split('old ')[1].split()[1],
        'div': int(monkey[3].split('by ')[1]),
        'true': int(monkey[4].split('monkey ')[1]),
        'false': int(monkey[5].split('monkey ')[1]),
    }
 
def main():
    monkeys = [gen_monkey([y.strip() for y in x.split('\n')]) for x in open('../input.txt').read().split('\n\n')]
    
    print(f'Silver: {silver(copy.deepcopy(monkeys))}')
    print(f'Gold: {gold(monkeys)}')

def silver(monkeys):
    inspection = [0 for _ in monkeys]
 
    for _ in range(20):
        for idx, monkey in enumerate(monkeys):
            for _ in range(len(monkey['items'])):
                inspection[idx] += 1
                increase_worry_level(monkey)
                control_worry_level(monkey, None)
                move_item(monkey, monkeys, is_divisible(monkey))
 
    return prod(sorted(inspection, reverse=True)[:2])

def gold(monkeys):
    inspection = [0 for _ in monkeys]
 
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            for _ in range(len(monkey['items'])):
                inspection[i] += 1
                increase_worry_level(monkey)
                control_worry_level(monkey, prod([x['div'] for x in monkeys]))
                move_item(monkey, monkeys, is_divisible(monkey))
 
    return prod(sorted(inspection, reverse=True)[:2])
 
if __name__ == '__main__':
    main()
