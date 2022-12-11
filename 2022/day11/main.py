
from math import prod
from time import sleep
from operator import add, mul, floordiv, mod
from functools import partial
from collections import deque


def debug(monkeys):
    for index, monkey in enumerate(monkeys):
        print(index, monkey['items'])
    sleep(1)


def solve2(monkeys, rounds, testprod):
    for _ in range(rounds):
        for monkey in monkeys:
            for item in map(monkey['operation'], monkey['items']):
                monkey['count'] += 1

                item %= testprod

                if item % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)

            monkey['items'] = []

    return prod(list(sorted([monkey['count'] for monkey in monkeys]))[-2:])


def solve1(monkeys, rounds):
    for _ in range(rounds):
        #debug(monkeys)
        for monkey in monkeys:
            for item in map(monkey['operation'], monkey['items']):
                monkey['count'] += 1

                item = item // 3

                if item % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)

            monkey['items'] = []

    return prod(list(sorted([monkey['count'] for monkey in monkeys]))[-2:])


def solve(monkeys, rounds, op, number):
    for _ in range(rounds):
        #debug(monkeys)
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
    # for _ in range(rounds):
    #     #debug(monkeys)
    #     for index, monkey in enumerate(monkeys):
    #         while monkey['items']:
    #             monkey['count'] += 1
                
    #             item = op(monkey['operation'](monkey['items'].popleft()), number)

    #             if item % monkey['test'] == 0:
    #                 monkeys[monkey['true']]['items'].append(item)
    #             else:
    #                 monkeys[monkey['false']]['items'].append(item)

    # return prod(list(sorted([monkey['count'] for monkey in monkeys]))[-2:])


def main():
    input = [monkey.split('\n') for monkey in open('input2.txt').read().split('\n\n')]

    monkeys = []

    for lines in input:
        monkey = {
            'count': 0,
            'items': deque(map(int, lines[1].split(':')[1].split(','))),
            'test': int(lines[3].split()[-1]),
            'true': int(lines[4].split()[-1]),
            'false': int(lines[5].split()[-1]),
        }

        operation = lines[2].split('=')[1].split()

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


    print(solve(monkeys, 20, floordiv, 3))
    print(solve(monkeys, 10000, mod, lcm))

if __name__ == "__main__":
    main()