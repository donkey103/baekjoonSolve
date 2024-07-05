import sys
line = sys.stdin.readline()
while line:
  a, b = map(int, line.strip().split())
  print(a+b)
  line = sys.stdin.readline()
  
  
