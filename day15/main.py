from math import inf
from collections import defaultdict
from queue import PriorityQueue


class Graph():
    def __init__(self, grid):
        self._graph = defaultdict(dict)
        self._build(self._pad(grid, inf))

    def _build(self, grid):
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[y]) - 1):
                self._graph[(y, x)][(y - 1, x)] = grid[y - 1][x]
                self._graph[(y, x)][(y + 1, x)] = grid[y + 1][x]
                self._graph[(y, x)][(y, x - 1)] = grid[y][x - 1]
                self._graph[(y, x)][(y, x + 1)] = grid[y][x + 1]


    def _pad(self, array, pad):
        newarray = []

        for line in array:
            newarray.append([pad] + [int(c) for c in line] + [pad])

        xlen = len(newarray[0])
        row = [pad] * xlen
        newarray = [row] + newarray + [row]

        return newarray


    def find_shortest(self, start, end):
        visited = set()
        distances = { v: inf for v in self._graph }
        distances[start] = 0

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            (dist, current) = pq.get()
            visited.add(current)

            for neighbour in self._graph[current]:
                if self._graph[current][neighbour] != inf and neighbour not in visited:
                    distance = self._graph[current][neighbour]
                    old_cost = distances[neighbour]
                    new_cost = distances[current] + distance
                    
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbour))
                        distances[neighbour] = new_cost

        return distances[end]


def increment_grid(grid, number):
    new_grid = grid.copy()
    
    for y in grid:
        for x in y:
            new_grid[y][x] += number

            if new_grid[y][x] > 9:
                new_grid[y][x] = new_grid[y][x] - 9

    return new_grid


def increment_row(row, risk):
    new_row = row.copy()

    for x in range(len(row)):
        new_row[x] += risk

        if new_row[x] > 9:
            new_row[x] = new_row[x] - 9

    return new_row


def transform_grid(grid):
    new_rows = []
    new_grid = []

    for y in grid:
        new_rows.append(y + increment_row(y, 1) + increment_row(y, 2) + increment_row(y, 3) + increment_row(y, 4))

    for i in range(5):
        for y in new_rows:
            new_grid.append(increment_row(y, i))

    return new_grid
        


def main():
    grid = [[int(x) for x in y] for y in [l.rstrip() for l in open("input.txt").readlines()]]
    new_grid = transform_grid(grid)

    graph = Graph(grid)
    graph_2 = Graph(new_grid)

    print(graph.find_shortest((1, 1), (len(grid), len(grid[0]))))
    print(graph_2.find_shortest((1, 1), (len(new_grid), len(new_grid[0]))))


if __name__ == "__main__":
    main()