total = int(input())
num = int(input())

sum = 0
for i in range(num):
  price, count = map(int, input().split())
  sum += price * count

if total == sum:
  print('Yes')
else:
  print('No')