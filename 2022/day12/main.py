from math import inf
from copy import deepcopy
from queue import PriorityQueue
from collections import defaultdict


class Graph():
    def __init__(self, grid):
        self._graph = defaultdict(dict)
        self._build(grid)


    def _build(self, grid):
        h, w = len(grid), len(grid[0])
        for y in range(0, h):
            for x in range(0, w):
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < w and 0 <= ny < h:
                        self._graph[(y, x)][(ny, nx)] = inf if ord(grid[ny][nx]) - ord(grid[y][x]) > 1 else 1


    def find_shortest(self, start, end):
        visited = set()
        distances = defaultdict(lambda: inf, {start: 0})

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            (current_dist, current) = pq.get()
            visited.add(current)

            for neighbour in self._graph[current]:
                if neighbour not in visited:
                    distance = self._graph[current][neighbour]
                    old_cost = distances[neighbour]
                    new_cost = current_dist + distance
                    
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbour))
                        distances[neighbour] = new_cost

        return distances[end]

def solve1(grid):
    h, w = len(grid), len(grid[0])
    for y in range(0, h):
        for x in range(0, w):
            if grid[y][x] == 'E':
                end = (y, x)
                grid[y][x] = 'z'
            if grid[y][x] == 'S':
                start = (y, x)
                grid[y][x] = 'a'

    graph = Graph(grid)

    return graph.find_shortest(start, end)


def solve2(grid):
    shortest = []

    h, w = len(grid), len(grid[0])
    for y in range(0, h):
        for x in range(0, w):
            if grid[y][x] == 'E':
                end = (y, x)
                grid[y][x] = 'z'
            if grid[y][x] == 'S':
                grid[y][x] = 'a'

    graph = Graph(grid)

    for y in range(0, h):
        for x in range(0, w):
            if grid[y][x] == 'a':
                shortest.append(graph.find_shortest((y, x), end))

    return min(shortest)


def main():
    grid = [list(line.strip()) for line in open('input.txt')]

    print(solve1(deepcopy(grid)))
    print(solve2(deepcopy(grid)))


if __name__ == "__main__":
    main()