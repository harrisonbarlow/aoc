import numpy as np

def solve2(input):
    views = []

    for iy, ix in np.ndindex(input.shape):
        left = input[iy,:ix][::-1]
        right = input[iy,ix+1:]
        top = input[:iy, ix][::-1]
        bottom = input[iy+1:, ix]

        height = input[iy, ix]

        score = 1
        
        for line in [top, bottom, left, right]:
            counter = 0

            for tree in line:
                counter += 1

                if tree >= height:
                    break

            score *= counter

        views.append(score)

    return max(views)


def solve1(input):
    visible = 0

    for iy, ix in np.ndindex(input.shape):
        left = input[iy,:ix]
        right = input[iy,ix+1:]
        top = input[:iy, ix]
        bottom = input[iy+1:, ix]

        height = input[iy, ix]
        
        if not any(filter(lambda h: h >= height, top)) or \
           not any(filter(lambda h: h >= height, bottom)) or \
           not any(filter(lambda h: h >= height, left)) or \
           not any(filter(lambda h: h >= height, right)):
            visible += 1

    return visible


def main():
    input = np.array([list(line.strip()) for line in open('input.txt')])
    
    print(solve1(input))
    print(solve2(input))

if __name__ == "__main__":
    main()