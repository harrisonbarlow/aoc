import pdb

if __name__ == "__main__":
    counter = [0] * 5
    for line in open("input2.txt"):
        trimmed = line.strip()
        for index, char in enumerate(trimmed):
            if char == "0":
                counter[index] = counter[index] - 1
            else:
                counter[index] = counter[index] + 1

    print(counter)

    # gamma, epsilon = "", ""
    # for num in counter:
    #     if num < 0:
    #         gamma += "0"
    #         epsilon += "1"
    #     else:
    #         gamma += "1"
    #         epsilon += "0"

    # print(int(gamma, 2))

    # print(int(epsilon, 2))
    # MOST_COMMON = "10110"
    # LEAST_COMMON = "01001"
    # # MOST_COMMON = "011101001101"
    # # LEAST_COMMON = "100010110010"

    # numbers = []
    # remove = []

    # for line in open("input2.txt"):
    #     numbers.append(line.rstrip())

    # for index, char in enumerate(MOST_COMMON):
    #     for number in numbers:
    #         #pdb.set_trace()
    #         if number[index] != char:
    #             remove.append(number)
    #             if list(set(numbers).intersection(remove)) == 1:
    #                 print(list(set(numbers).intersection(remove)))

    # # for index, char in enumerate(LEAST_COMMON):
    # #     for number in numbers:
    # #         if number[index] != char:
    # #             numbers.remove(number)

    # print(numbers)