import re
from itertools import cycle, count
from math import lcm


def traverse(instructions, network, start, end):
    node = start

    for step, direction in zip(count(0), cycle(instructions)):
        if node in end:
            return step

        node = network[node][direction]


def main():
    instructions, _, *nodes = open('input.txt').read().split('\n')

    network = {}

    for line in nodes:
        node, left, right = re.findall(r'\w+', line)

        network[node] = {'L': left, 'R': right}

    starts = [node for node in network if node.endswith('A')]
    ends = [node for node in network if node.endswith('Z')]

    print(traverse(instructions, network, 'AAA', ['ZZZ']))
    print(lcm(*(traverse(instructions, network, start, ends) for start in starts)))


if __name__ == '__main__':
    main()