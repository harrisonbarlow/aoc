
def solve2(x_target, y_target):
    (min_x, max_x) = x_target
    (min_y, max_y) = y_target

    def brute_force(vx, vy):
        x, y = 0, 0

        while y > -min_y:
            #print(x,y)
            x += vx
            y += vy

            if vx > 0:
                vx -= 1

            vy -= 1

            if min_x <= x <= max_x and -min_y <= y <= -max_y:
                return 1

        return 0

    return sum(brute_force(vx, vy) for vx in range(1, max_x + 1) for vy in range(-min_y, min_y))



def solve1(x_target, y_target):
    min_x, max_x = x_target
    min_y, max_y = y_target

    return min_y * (min_y + 1) // 2


def main():
    x_range, y_range = open("input2.txt").read().rstrip().replace('target area: ', '').split(',')

    x_target = tuple(map(int, x_range.replace('x=', '').split('..')))
    y_target = tuple(map(int, y_range.lstrip().replace('y=', '').split('..')))

    print(solve1(x_target, y_target))
    print(solve2(x_target, y_target))

if __name__ == "__main__":
    main()