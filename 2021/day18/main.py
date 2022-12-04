from ast import literal_eval
from math import floor, ceil

class Node():
    def __init__(self, data, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self._build(data)


    def __repr__(self):
        return f"[{self.left}, {self.right}]"


    def __add__(self, node):
        result = Node(eval(f"[{str(self)}, {str(node)}]"))

        while True:
            exploded = result._explode()
            if not exploded:
                if not result._split():
                    break

        return result


    def __abs__(self):
        if isinstance(self.left, int):
            return self.left
        if isinstance(self.right, int):
            return self.right

        return 3 * abs(self.left) + 2 * abs(self.right)


    def _build(self, data):
        if type(data[0]) is int:
            self.left = data[0]
        else:
            self.left = Node(data[0], self)

        if type(data[1]) is int:
            self.right = data[1]
        else:
            self.right = Node(data[1], self)


    def _is_leaf(self):
        return isinstance(self.left, int) and isinstance(self.right, int)


    def _explode_right(self, node, number):
        current_node = node
        prev_node = node.right

        while current_node != None and (current_node.right == prev_node or current_node.right == None):
            prev_node = current_node
            current_node = current_node.parent

        if current_node != None:
            current_node == current_node.right

            while isinstance(current_node, Node):
                if isinstance(current_node.right, int):
                    break
                else:
                    current_node = current_node.right

            current_node.right += number


    def _explode_left(self, node, number):
        current_node = node
        prev_node = node.left

        while current_node != None and (current_node.left == prev_node or current_node.left == None):
            prev_node = current_node
            current_node = current_node.parent

        if current_node != None:
            current_node == current_node.left

            while isinstance(current_node, Node):
                if isinstance(current_node.left, int):
                    break
                else:
                    current_node = current_node.left

            current_node.left += number


    def _explode(self, level=-1):
        level = level + 1

        if self._is_leaf:
            return False, None, None

        if level == 4:
            self._explode_left(self, self.left)
            self._explode_right(self, self.right)
            return True, self.left, self.right

        exploded, left, right = self.left.explode(level)
        if exploded:
            self._explode_left(self, left)
            return True, None, None
        exploded, left, right = self.right.explode(level)
        if exploded:
            self._explode_right(self, right)
            return True, None, None

        return False, None, None


    def _split(self, node, split=False):
        if type(node.left) is int:
            val = node.left
            if val >= 10 and not split:
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

        return split


    def reduce(self):
        # print(self)
        # exploded = self._explode(self)
        # split = self._split(self)

        # if exploded or split:
        #     self.reduce()
        self._explode(self)
        


def solve1(numbers):
    root = Node(numbers[0], 0)
    
    for number in range(1, len(numbers)):
        root = root + numbers[number]

    return abs(root)


def main():
    numbers = [literal_eval(l.rstrip()) for l in open("input2.txt").readlines()]
    print(solve1(numbers))


if __name__ == "__main__":
    main()