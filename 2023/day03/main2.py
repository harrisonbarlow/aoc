import re
from math import prod

def solve1(graph):
    return sum(sum(p) for p in graph.values())


def solve2(graph):
    return sum(prod(p) for p in graph.values() if len(p)==2)


def main():
    lines = [line.rstrip() for line in open('input2.txt')]

    graph = {
        (y, x): []
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char not in '01234566789.'
    }

    for y, line in enumerate(lines):
        for num in re.finditer(r'\d+', line):
            edge = {
                (r, c) 
                for r in (y - 1, y, y + 1)
                for c in range(num.start() - 1, num.end() + 1)
            }

            for o in edge & graph.keys():
                graph[o].append(int(num.group()))


    print(solve1(graph))
    print(solve2(graph))


if __name__ == '__main__':
    main()