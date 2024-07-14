import sys
numberList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, sys.stdin.readline().split())

arr = []
while n > 0:
  mod = n % b
  arr.append(numberList[mod])
  n = n // b
arr.reverse()
print(''.join(arr))