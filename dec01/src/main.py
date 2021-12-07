


if __name__ == "__main__":
    a = []
    sliding = []
    lines = open("../input.txt", "r")
    counter = 0
    for line in lines:
        a.append(int(line.strip()))

    # for index, element in enumerate(array):
    #     if index > 1:
    #         sliding.append(array[index] + array[index - 1] + array[index - 2])

    # for index, element in enumerate(sliding):
    #     if index > 0:
    #         if sliding[index] > sliding[index-1]:
    #             counter = counter + 1
    # print(counter)
    f=lambda a:sum(x<y for x,y in zip(a,a[1:]))
    g=lambda a:sum(x<y for x,y in zip(a,a[3:]))

    print(sum((x<y)+1j*(x<z) for x,y,z in zip(a,a[1:],a[3:])))