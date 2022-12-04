import math

s = set()
def f(h, y, x):
  if h[y][x] != 9 and (y,x) not in s:
    s.add((y,x))
    return 1+f(h,y-1,x)+f(h,y+1,x)+f(h,y,x-1)+f(h,y,x+1)
  else:
    return 0


def a(h):
  b = set()
  for y in range(1, len(h) -1):
    for x in range(1, len(h[y]) - 1):
      b.add(f(h, y, x))
  return math.prod(list(b)[-3:])


def p(a, n):
  b = []

  for l in a:
    b.append([n] + [int(c) for c in l] + [n])

  m = len(b[0])
  r = [n] * m
  b = [r] + b + [r]

  return b


def main():
  h = list(map(list, open("input.txt").read().rstrip().split("\n")))
  print(a(p(h, 9)))


if __name__ == "__main__":
  main()