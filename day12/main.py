from collections import defaultdict

class Graph():
    def __init__(self, edges):
        self._graph = defaultdict(set)
        self.add_edges(edges)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


    def add_edges(self, edges):
        for [node1, node2] in edges:
            self._graph[node1].add(node2)
            self._graph[node2].add(node1)


    def solve1(self, node1, node2, path=[], paths=[], visited=[]):
        path = path + [node1]

        if node1 in visited:
            return

        if node1.islower():
            visited = visited + [node1]

        if node1 == node2:
            paths.append(path)
            return

        for node in self._graph[node1]:
            self.solve1(node, node2, path, paths, visited)

        return len(paths)


    def solve2(self, node1, node2, path=[], paths=[], visited=[]):
        path = path + [node1]

        if node1 == "start" and node1 in visited:
            #Already been to the start, exit
            return

        if node1 == "end" and node1 in visited:
            #already been to the end, exit
            return

        if visited.count(node1) == 2:
            #Already been here twice, exit
            return

        if node1.islower():
            visited = visited + [node1]
            if len(visited) > len(set(visited)) + 1:
                #Already visited another node twice, exit
                return

        if node1 == node2:
            #Arrived at the end, append path to list of viable paths
            paths.append(path)
            return

        for node in self._graph[node1]:
            self.solve2(node, node2, path, paths, visited)


        return len(paths)


def main():
    edges = [e.split('-') for e in [l.rstrip() for l in open("input.txt").readlines()]]

    graph = Graph(edges)

    print(graph.solve1("start", "end"))
    print(graph.solve2("start", "end"))

    

if __name__ == "__main__":
    main()