num = int(input())

primeFactorList = []
i = 2
while i <= num ** (1/2):
  if num % i == 0:
    primeFactorList.append(i)
    num //= i
    i = 2
  else:
    i += 1
if num > 1:
  primeFactorList.append(num)
 
for el in primeFactorList:
  print(el)

  