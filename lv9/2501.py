import math
n, k = map(int, input().split())

factorList = []
sqrtNum = math.sqrt(n)
loop = 1
while loop <= sqrtNum:
  if n % loop == 0:
    factorList.append(loop)
    if loop != sqrtNum:
      factorList.append(int(n / loop))
  loop += 1
factorList.sort()
if k <= len(factorList):
  print(factorList[k-1])
else:
  print(0)