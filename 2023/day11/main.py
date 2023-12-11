def compute_distance(rows, columns, start, end, distance):
    y1, x1 = start
    y2, x2 = end

    x_distance = 0
    y_distance = 0

    for y in range(min(y1, y2), max(y1, y2)):
        x_distance += distance if len(rows[y]) == 1 else 1

    for x in range(min(x1, x2), max(x1, x2)):
        y_distance += distance if len(columns[x]) == 1 else 1

    return x_distance + y_distance


def solve(input, distance):
    graph = {}

    rows = [set(line) for line in input]
    columns = [set(line) for line in zip(*input)]

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '#':
                graph[(y, x)] = {}

                for node in graph:
                    if node != (y, x):
                        graph[node][(y, x)] = compute_distance(rows, columns, node, (y, x), distance)
    
    return sum([sum(graph[node].values()) for node in graph])


def main():
    input = [list(line) for line in open('input.txt').read().split('\n')]

    print(solve(input, 2))
    print(solve(input, 1000000))


if __name__ == '__main__':
    main()