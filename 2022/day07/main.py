import re

class Node:
    def __init__(self, folder, parent=None):
        self.folder = folder
        self.parent = parent
        self.children = []
        self.size = 0

    def add_size(self, size):
        self.size += int(size)

        if self.parent is not None:
            self.parent.add_size(size)

        return self

    def add_child(self, folder):
        new = Node(folder, self)
        self.children.append(new)

        return new


def flatten(node, nodes=[]):
    nodes.append(node.size)

    for child in node.children:
        flatten(child)

    return nodes


def change_directory(match, current):
    folder = match.group(1)

    if folder == '..':
        return current.parent
    else:
        return current.add_child(folder)


def found_file(match, current):
    size, filename = match.group(1), match.group(2)

    return current.add_size(size)


def solve1(root):    
    return sum(node for node in flatten(root) if node <= 100000)


def solve2(root):
    nodes = sorted(flatten(root))
    return [node for node in nodes if node > nodes[-1] - 40000000][0]


def main():
    input = [line.rstrip() for line in open('input.txt').readlines()]

    root = Node(input[0])
    current = root

    patterns = {
        '\$ cd (.*)': change_directory,
        '(\d+) (.*)': found_file,
    }

    for line in input[1:]:
        for pattern in patterns:
            match = re.match(pattern, line)

            if match is not None:
                current = patterns[pattern](match, current)

    print(solve1(root))
    print(solve2(root))


if __name__ == "__main__":
    main()