import math
import json

from math import prod
from time import sleep
from operator import add, mul, mod
from functools import partial


def debug(monkeys):
    for index, monkey in enumerate(monkeys):
        print(index, monkey['items'])
    sleep(1)

def solve1(monkeys):
    for _ in range(20):
        for index, monkey in enumerate(monkeys):
            monkey['items'] = list(map(monkey['operation'], monkey['items']))
            monkey['items'] = list(map(lambda x: x // 3, monkey['items']))

            for item in monkey['items']:
                monkey['count'] += 1

                print(item, monkey['test'](item))
                if monkey['test'](item):
                    monkeys[monkey['true']]['items'].append(item)
                    print(f"Throwing {item} to {monkey['true']}")
                else:
                    monkeys[monkey['false']]['items'].append(item)
                    print(f"Throwing {item} to {monkey['false']}")

            monkey['items'] = []

        debug(monkeys)

    #print(list(reversed(sorted([monkey['count'] for monkey in monkeys])))[0:2])
    print(list(reversed(sorted([monkey['count'] for monkey in monkeys]))))
    return prod(list(reversed(sorted([monkey['count'] for monkey in monkeys])))[0:2])


def square(n):
    return n * n


def main():
    input = [monkey.split('\n') for monkey in open('input2.txt').read().split('\n\n')]

    monkeys = []

    for lines in input:
        monkey = {'count': 0}
        monkey['items'] = list(map(int, lines[1].split(':')[1].split(',')))
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

        test = lines[3].split()
        test_num = int(test[-1])
        monkey['test'] = lambda x: (x / test_num).is_integer()

        true = lines[4].split()
        monkey['true'] = int(true[-1])

        false = lines[5].split()
        monkey['false'] = int(false[-1])

        #print(decision)

        monkeys.append(monkey)

    print(solve1(monkeys))

if __name__ == "__main__":
    main()