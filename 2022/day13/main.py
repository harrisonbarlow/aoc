from time import sleep


def compare_lists(left_list, right_list):
    #result = False
    print(f"Comparing: {left_list} and {right_list}")
    #sleep(1)

    for left, right in zip(left_list, right_list):
        if isinstance(left, int) and isinstance(right, int):
            print(f"Comparing: {left} and {right}")
            if left < right:
                print("Right order")
                return True
            elif left > right:
                print("Wrong order")
                return False
            else:
                continue

        if compare_lists(left if isinstance(left, list) else [left], right if isinstance(right, list) else [right]):
            continue
        else:
            break
                
    else:
        #- Left side ran out of items, so inputs are in the right order
        #- Right side ran out of items, so inputs are not in the right order
        if len(left_list) <= len(right_list):
            return True

    #print(f"Result was {result}")

    return False


def solve1(packets):
    correct = []
    for index, (left, right) in enumerate(packets):
        if compare_lists(left, right):
            correct.append(index + 1)
        print()

    print(correct)

    return sum(correct)


def main():
    packets = [(eval(left.strip()), eval(right.strip())) for left, right in [pair.split() for pair in open('input2.txt').read().split('\n\n')]]

    #print(packets)

    print(solve1(packets))


if __name__ == "__main__":
    main()