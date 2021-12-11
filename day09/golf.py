import math

d = dict()
def f(h, y, x):
  if h[y][x] != 9 and (y,x) not in d:
    d[(y,x)] = True
    return 1 + f(h,y-1,x)+f(h,y+1,x)+f(h,y,x-1)+f(h,y,x+1)
  else:
    return 0

def s(h):
  s = set()
  for y in range(1, len(h) -1):
    for x in range(1, len(h[y]) - 1):
      s.add(f(h, y, x))
  return math.prod(list(s)[-3:])

def pad(array, pad):
  newarray = []

  for line in array:
    newarray.append([pad] + [int(c) for c in line] + [pad])

  xlen = len(newarray[0])
  row = [pad] * xlen
  newarray = [row] + newarray + [row]

  return newarray

def main():
  heights = list(map(list, open("input.txt").read().rstrip().split("\n")))

  print(s(pad(heights, 9)))


if __name__ == "__main__":
  main()