def getDigitSum(num):
  sum = 0
  while num > 0:
    sum += num % 10
    num //= 10
  return sum

num = int(input())
constructors = []
for i in range(num - 1, max(num - 55, 0), - 1):

  if (i + getDigitSum(i))  == num:
    constructors.append(i)
    
if len(constructors) == 0:
  print(0)
else:
  print(constructors[-1])
