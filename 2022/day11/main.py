from math import prod
from copy import deepcopy
from operator import floordiv, mod

def solve(monkeys, rounds, op, number):
    for _ in range(rounds):
        for monkey in monkeys:
            for item in map(monkey['operation'], monkey['items']):
                monkey['count'] += 1

                item = op(item, number)

                if item % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)

            monkey['items'] = []

    return prod(list(sorted([monkey['count'] for monkey in monkeys]))[-2:])


def main():
    input = [block.split('\n') for block in open('input.txt').read().split('\n\n')]

    monkeys = []

    for block in input:
        monkeys.append({
            'count': 0,
            'items': list(map(int, block[1].split(':')[1].split(','))),
            'operation': eval('lambda old: ' + block[2].split('= ')[1]),
            'test': int(block[3].split()[-1]),
            'true': int(block[4].split()[-1]),
            'false': int(block[5].split()[-1])
        })

    lcm = prod([monkey['test'] for monkey in monkeys])

    print(solve(deepcopy(monkeys), 20, floordiv, 3))
    print(solve(deepcopy(monkeys), 10000, mod, lcm))

if __name__ == "__main__":
    main()