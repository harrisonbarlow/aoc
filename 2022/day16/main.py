from math import inf
from queue import PriorityQueue
from collections import defaultdict



class Graph:
    def __init__(self, valves):
        self._graph = self._build(valves)

    def _build(self, valves):
        graph = defaultdict(dict)

        for valve in valves:
            for lead in valves[valve]['leads']:
                graph[valve][lead] = 1

        return graph

    def find_shortest(self, start):
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

        return distances


def solve1(valves):
    graph = Graph(valves)
    distances = {}

    for valve in valves:
        distances[valve] = graph.find_shortest(valve)

    print(distances)

# def search(valves, valve, minute, open=set(), pressure=0, pressures=[]):
#     if minute == 30:
#         pressure

#     open = open | set((valve,))

#     print(valve, open)

#     for currently_open in open:
#         pressure += valves[currently_open]['flow']
#         pressures.append(pressure)


#     for neighbour in valves[valve]['leads']:
#         search(valves, neighbour, minute + 1, open, pressure)

#     return max(pressures)


# def solve1(valves):
#     print(valves)
#     return search(valves, 'AA', 1)



def main():
    valves = {}
    for line in open('input2.txt'):
        _, valve, _, _, flow, _, _, _, _, *leads = line.split()

        valves[valve] = {
            'flow': int(flow.rstrip(';').split('=')[1]),
            'leads': [lead.strip(',') for lead in leads]
        }


    print(solve1(valves))


if __name__ == "__main__":
    main()