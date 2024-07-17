num = int(input())

primeFactorList = []
i = 2
while True:
  if num % i == 0:
    primeFactorList.append(i)
    num /= i
    i = 2
  else:
    i += 1

for el in primeFactorList:
  print(el)