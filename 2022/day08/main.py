
def search_left(input, y, x, height):
    if 0 <= x - 1 < len(input[y]):
        if input[y][x-1] >= height:
            return False
        else:
            return search_left(input, y, x-1, height)
    else:
        return True

def search_right(input, y, x, height):
    if 0 <= x + 1 < len(input[y]):
        if input[y][x+1] >= height:
            return False
        else:
            return search_right(input, y, x+1, height)
    else:
        return True

def search_top(input, y, x, height):
    if 0 <= y - 1 < len(input):
        if input[y-1][x] >= height:
            return False
        else:
            return search_top(input, y-1, x, height)
    else:
        return True


def search_bottom(input, y, x, height):
    if 0 <= y + 1 < len(input):
        if input[y+1][x] >= height:
            return False
        else:
            return search_bottom(input, y+1, x, height)
    else:
        return True



def view_top(input, y, x, height):
    if 0 <= y - 1 < len(input):
        if input[y-1][x] >= height:
            return 1
        else:
            return 1 + view_top(input, y-1, x, height)
    else:
        return 0


def view_bottom(input, y, x, height):
    if 0 <= y + 1 < len(input):
        if input[y+1][x] >= height:
            return 1
        else:
            return 1 + view_bottom(input, y+1, x, height)
    else:
        return 0

def view_left(input, y, x, height):
    if 0 <= x - 1 < len(input[y]):
        if input[y][x-1] >= height:
            return 1
        else:
            return 1 + view_left(input, y, x-1, height)
    else:
        return 0

def view_right(input, y, x, height):
    if 0 <= x + 1 < len(input[y]):
        if input[y][x+1] >= height:
            return 1
        else:
            return 1 + view_right(input, y, x+1, height)
    else:
        return 0
        


def solve2(input):
    views = []

    for y, row in enumerate(input):
        for x, height in enumerate(row):
            views.append(view_top(input, y, x, height) * view_bottom(input, y, x, height) * view_left(input, y, x, height) * view_right(input, y, x, height))

    return max(views)



# def solve1(input):
#     visible = 0
#     for y, row in enumerate(input):
#         for x, height in enumerate(row):
#             if search_top(input, y, x, height) or search_bottom(input, y, x, height) or search_left(input, y, x, height) or search_right(input, y, x, height):
#                 #print(y, x)
#                 visible += 1

#     return visible


def solve1(input):
    visible = 0

    for y, row in enumerate(input):
        for x, height in enumerate(row):
            left = row[:x] if x > 0 else []
            right = row[x+1:]
            top = [row[x] for row in input[:y]] if y > 0 else []
            bottom = [row[x] for row in input[y+1:]]

            #print(top, bottom, left, right)

            if any(filter(lambda h: h >= height, top)) or any(filter(lambda h: h >= height, bottom)) or any(filter(lambda h: h >= height, left)) or any(filter(lambda h: h >= height, right)):
                visible += 1


    return visible

def main():
    input = [[int(x) for x in y] for y in [line.rstrip() for line in open('input.txt')]]

    print(solve1(input))
    #print(solve2(input))


if __name__ == "__main__":
    main()