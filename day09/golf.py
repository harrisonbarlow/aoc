import math

d = dict()
def f(h, x, y):
  if h[y][x] != 9 and f"{x},{y}" not in d:
    d[f"{x},{y}"] = True
    return 1 + f(h,x,y-1)+f(h,x,y+1)+f(h,x-1,y)+f(h,x+1,y)
  else:
    return 0

def s(h):
  s = set()
  for y in range(1, len(h) -1):
    for x in range(1, len(h[y]) - 1):
      s.add(f(h, x, y))
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