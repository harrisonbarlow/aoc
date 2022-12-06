def solve(stream, num):
    for i in range(num, len(stream)):
        if num == len(set(stream[i-num:i])):
            return i

def main():
    stream = open('input.txt').read()

    print(solve(stream, 4))
    print(solve(stream, 14))


if __name__ == "__main__":
    main()