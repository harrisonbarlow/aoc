directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

pipes = {
    '|': {
        'U': 'U',
        'D': 'D',
    },
    '-': {
        'L': 'L',
        'R': 'R',
    },
    'L': {
        'D': 'R',
        'L': 'U',
    },
    'J': {
        'R': 'U',
        'D': 'L',
    },
    '7': {
        'R': 'D',
        'U': 'L',
    },
    'F': {
        'U': 'R',
        'L': 'D',
    },
}


def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def solve2(input, graph, start):
    direction = 'D'

    node = add_tuple(start, directions[direction])
    vitited = set([start, node])

    while node != start:
        val = graph[node]
        direction = pipes[val][direction]
        node = add_tuple(node, directions[direction])
        vitited.add(node)


    parity = 0
    last = None
    outside = []

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            node = (y, x)

            if node in vitited:
                if (
                    (last == 'L' and c == '7') or 
                    (last == 'F' and c == 'J') or 
                    c in ['|', 'S']
                ):
                    parity += 1

                if c in ['L', 'F']:
                    last = c

            else:
                if parity % 2 != 0:
                    outside.append(node)

        parity = 0


    return len(outside)


def solve1(graph, start):
    direction = 'D'

    node = add_tuple(start, directions[direction])

    length = 1

    while node != start:
        val = graph[node]
        direction = pipes[val][direction]
        node = add_tuple(node, directions[direction])
        length += 1

    return length // 2


def main():
    input = [list(line) for line in open('input5.txt').read().splitlines()]

    graph = {}

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            graph[(y, x)] = c

            if c == 'S':
                start = (y, x)

    print(solve1(graph, start))
    print(solve2(input, graph, start))


if __name__ == '__main__':
    main()