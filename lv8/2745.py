numberList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()

sum = 0
for idx in range(len(n)):
  num = numberList.index(n[idx]) * (int(b) ** (len(n) - 1 - idx))
  print(num)
  sum += num
print(sum)