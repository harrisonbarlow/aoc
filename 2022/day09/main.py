import numpy as np

def solve(steps, length):
    dirs = {
        'U': [0, 1],
        'D': [0, -1],
        'L': [-1 ,0],
        'R': [1, 0]
    }

    visited = set()
    knots = [np.array([0, 0]) for _ in range(length)]

    for dir, step in steps:
        for _ in range(int(step)):
            knots[0] += dirs[dir]

            for prev, curr in zip(knots, knots[1:]):
                if max(abs(prev - curr)) > 1:
                    curr += np.clip((prev - curr), -1, 1)

            visited.add(tuple(knots[-1]))

    return len(visited)


def main():
    steps = [step.split() for step in open('input.txt')]

    print(solve(steps, 2))
    print(solve(steps, 10))


if __name__ == "__main__":
    main()