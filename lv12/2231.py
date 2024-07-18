num = int(input())
constructors = []
for i in range(10):
  for j in range(10):
    for k in range(10):
      for x in range(10):
        for y in range(10):
          for z in range(10):
            if i == 0 and j == 0 and k == 0 and x == 0 and y == 0 and z == 0:
              continue
            newNum = num - i - j - k - x - y - z
            if newNum == 100000 * i + 10000 * j + 1000 * k + 100 * x + 10 * y + z:
              constructors.append(newNum)
if len(constructors) == 0:
  print(0)
else:
  print(sorted(constructors)[0])