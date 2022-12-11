
from math import prod
from copy import deepcopy, copy
from operator import add, mul, floordiv, mod
from functools import partial


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
    input = [monkey.split('\n') for monkey in open('input.txt').read().split('\n\n')]

    monkeys = []

    for block in input:
        monkey = {
            'count': 0,
            'items': list(map(int, block[1].split(':')[1].split(','))),
            'test': int(block[3].split()[-1]),
            'true': int(block[4].split()[-1]),
            'false': int(block[5].split()[-1]),
        }

        operation = block[2].split('=')[1].split()

        match operation[1]:
            case '*':
                match operation[2]:
                    case 'old':
                        monkey['operation'] = lambda x: x * x
                    case _:
                        monkey['operation'] = partial(mul, int(operation[2]))
            case '+':
                monkey['operation'] = partial(add, int(operation[2]))

        monkeys.append(monkey)

    lcm = prod([monkey['test'] for monkey in monkeys])

    print(solve(deepcopy(monkeys), 20, floordiv, 3))
    print(solve(deepcopy(monkeys), 10000, mod, lcm))

if __name__ == "__main__":
    main()