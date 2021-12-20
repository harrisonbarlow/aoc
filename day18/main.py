from math import floor, ceil


class Node():
    def __init__(self, number, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self._build(number)


    def __repr__(self):
        return f"{self.left}, {self.right}"


    def __add__(self, node):
        pass

    def _build(self, number):
        if type(number[0]) is int:
            self.left = number[0]
        else:
            self.left = Node(number[0], self)

        if type(number[1]) is int:
            self.right = number[1]
        else:
            self.right = Node(number[1], self)


    def add_right(self, node, number):
        if type(node) is int:
            node += number
            return

        self.add_right(node.left, number)


    def add_left(self, node, number):
        if type(node) is int:
            node += number
            return

        self.add_left(node.right, number)


    def _explode(self, node, level=0, exploded=False):
        #print(node)
        if level >= 2 and not exploded:
            if type(node.left) is int and type(node.right) is int:
                print(node)
                if node.parent.left != node:
                    self.add_left(node.parent.left, node.left)
                if node.parent.right != node:
                    self.add_right(node.parent.right, node.right)
                node = 0
                exploded = True
                return

        level = level + 1

        if type(node.left) is Node:
            self._explode(node.left, level)

        if type(node.right) is Node:
            self._explode(node.right, level)


    def _split(self, node, split=False):
        if type(node.left) is int:
            val = node.left
            if val > 10 and not split:
                node.left = Node([floor(val / 2), ceil(val / 2)], node)
                split = True
        else:
            self._split(node.left)

        if type(node.right) is int:
            val = node.right
            if val >= 10 and not split:
                node.right = Node([floor(val / 2), ceil(val / 2)], node)
                split = True
        else:
            self._split(node.right)


def solve1(numbers):
    tree = Node(numbers[0])
    print(tree)
    tree._explode(tree)
    print(tree)


def main():
    numbers = [eval(l.rstrip()) for l in open("input2.txt").readlines()]
    solve1(numbers)


if __name__ == "__main__":
    main()