import sys
input = sys.stdin.readline

loop = int(input())

for i in range(loop):
  a, b = map(int, input().split())
  print(a + b)
