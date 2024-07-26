import sys
n = int(sys.stdin.readline())
xMax = -99999
xMin = 99999
yMax = -99999
yMin = 99999
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  xMax = max(xMax, x)
  xMin = min(xMin, x)
  yMax = max(yMax, y)
  yMin = min(yMin, y)

print((xMax - xMin) * (yMax - yMin))