import math


def triangle(n):
    return int((n**2 + n) / 2)

def solve4(positions):
    low = min(positions)
    high = max(positions)

    while True:
        mid = (high + low) // 2
        fuel_right = 0
        fuel_left = 0

        print(f"Low: {low}")
        print(f"Mid: {mid}")
        print(f"High: {high}")

        for p in positions:
            if p > mid:
                fuel_right += triangle(abs(p - mid))
            if p < mid:
                fuel_left += triangle(abs(p - mid))

        if fuel_right > fuel_left:
            low = mid + 1
        elif fuel_right < fuel_left:
            high = mid - 1

        if high - low <= 1:
            return sum(triangle(abs(d - mid)) for d in positions)

        #sleep(1)

def calculate_fuel(crabs, pos):
    return sum(triangle(abs(pos - i)) for i in crabs)


def solve3(crabs):
    left = min(crabs)
    right = max(crabs)

    while left < right:
        mid = (left + right) // 2
        
        cost = sum(triangle(abs(mid - i)) for i in crabs)
        cost_right = sum(triangle(abs(mid + 1 - i)) for i in crabs)

        best = min(cost, cost_right)

        if cost_right >= cost:
            right = mid - 1
        else:
            left = mid + 1

    return best


def solve2(crabs):
    lowest = 999999999999

    for i in range(min(crabs), max(crabs)):
        sum = 0
        for j in crabs:
            sum += triangle(abs(i - j))
        
        if sum < lowest:
            lowest = sum

    return lowest


def solve1(crabs):
    lowest = 999999999999

    for i in crabs:
        sum = 0
        for j in crabs:
            sum += abs(i - j)
        
        if sum < lowest:
            lowest = sum

    return lowest


def main():
    crabs = list(map(int, open("input.txt").read().rstrip().split(",")))
    print(solve3(crabs))

if __name__ == "__main__":
    main()