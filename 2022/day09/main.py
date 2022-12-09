import math
from collections import defaultdict

def solve2(steps):
    visited = defaultdict(set)

    knots = []
    for _ in range(10):
        knots.append({'x': 0, 'y': 0})

    for index, knot in enumerate(knots):
        visited[index].add((knots[index]['x'], knots[index]['y']))
        #print(visited[index])

    for step in steps:
        #print(f"Processing Step: {step}")
        for _ in range(int(step[1])):

            match step[0]:
                case 'U':
                    knots[0]['y'] += 1
                case 'D':
                    knots[0]['y'] -= 1
                case 'L':
                    knots[0]['x'] -= 1
                case 'R':
                    knots[0]['x'] += 1


            for index in range(1, len(knots)):
                (dx, dy) = (knots[index - 1]['x'] - knots[index]['x'], knots[index - 1]['y'] - knots[index]['y'])
            
                if abs(dy) == 2 and abs(dx) == 1:
                    knots[index]['y'] += dy // 2
                    knots[index]['x'] += dx
                    continue

                if abs(dx) == 2 and abs(dy) == 1:
                    knots[index]['y'] += dy
                    knots[index]['x'] += dx // 2
                    continue

                if abs(dx) == 2 and abs(dy) == 2:
                    knots[index]['y'] += dy // 2
                    knots[index]['x'] += dx // 2
                    continue

                if abs(dx) == 2:
                    knots[index]['x'] += dx // 2
                    continue

                if abs(dy) == 2:
                    knots[index]['y'] += dy // 2
                    continue

            for index, knot in enumerate(knots):
                visited[index].add((knots[index]['x'], knots[index]['y']))

    return len(visited[9])

def solve1(steps):
    head = {
        'x': 0,
        'y': 0
    }

    tail = {
        'x': 0,
        'y': 0
    }

    visited = set()

    for step in steps:
        for _ in range(int(step[1])):
            visited.add((tail['x'], tail['y']))
            #print((head['x'], head['y']))   
            match step[0]:
                case 'U':
                    head['y'] += 1
                case 'D':
                    head['y'] -= 1
                case 'L':
                    head['x'] -= 1
                case 'R':
                    head['x'] += 1

            (dx, dy) = (head['x'] - tail['x'], head['y'] - tail['y'])

            if abs(dy) == 2 and abs(dx) == 1:
                tail['y'] += dy // 2
                tail['x'] += dx
                continue

            if abs(dx) == 2 and abs(dy) == 1:
                tail['x'] += dx // 2
                tail['y'] += dy
                continue

            if abs(dx) == 2:
                tail['x'] += dx // 2
                continue

            if abs(dy) == 2:
                tail['y'] += dy // 2
                continue
                
    return len(visited)



def main():
    steps = [step.split() for step in open('input.txt')]

    print(solve1(steps))
    print(solve2(steps))


if __name__ == "__main__":
    main()