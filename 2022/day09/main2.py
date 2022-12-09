lines = open('input3.txt', 'r').readlines()

import numpy

OFFSETS = {'L':(-1, 0), 'R':(1, 0), 'U':(0, -1), 'D':(0, 1)}

space = numpy.zeros(shape=(1000, 1000), dtype=numpy.int8)
headx, heady = 500, 500
tailx, taily = 500, 500


def sgn(x):
    if x == 0:
        return 0
    else:
        return x // abs(x)


knots = [(headx, tailx)] * 10

for line in lines:
    direction, steps = line.split()[0], int(line.split()[1])
    for i in range(steps):
        space[knots[9]] = 1
        knots[0] = (knots[0][0] + OFFSETS[direction][0], knots[0][1] + OFFSETS[direction][1])

        for j in range(1, 10):
            head = knots[j - 1]
            tail = knots[j]
            toffx, toffy = 0, 0
            if head[0] == tail[0]:
                if abs(head[1] - tail[1]) > 1:
                    toffy = sgn(head[1] - tail[1])
            elif head[1] == tail[1]:
                if abs(head[0] - tail[0]) > 1: 
                    toffx = sgn(head[0] - tail[0])
            else:
                if (abs(head[1] - tail[1]) > 1) or (abs(head[0] - tail[0]) > 1): 
                    toffx = sgn(head[0] - tail[0])
                    toffy = sgn(head[1] - tail[1])
            knots[j] = (tail[0] + toffx, tail[1] + toffy)

        print(knots)
        space[knots[9]] = 1  

print(space.sum())