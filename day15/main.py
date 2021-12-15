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
                        self._graph[(y, x)][(ny, nx)] = grid[ny][nx]


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


def transform(grid):
    h, w = len(grid), len(grid[0])

    for row in grid:
        for i in range(1, 5):
            row.extend([row[x] + i  if row[x] + i <= 9 else row[x] + i - 9 for x in range(w)])

    for i in range(1, 5):
        for row in range(h):
            grid.append([x + i if x + i <= 9 else x + i - 9 for x in grid[row]])
        
    return grid


def main():
    grid_1 = [[int(x) for x in y] for y in [l.rstrip() for l in open("input.txt").readlines()]]
    grid_2 = transform(deepcopy(grid_1))

    graph_1 = Graph(grid_1)
    graph_2 = Graph(grid_2)

    h_1, w_1 = len(grid_1) - 1, len(grid_1[0]) - 1
    h_2, w_2 = len(grid_2) - 1, len(grid_2[0]) - 1

    print(graph_1.find_shortest((0, 0), (h_1, w_1)))
    print(graph_2.find_shortest((0, 0), (h_2, w_2)))


if __name__ == "__main__":
    main()