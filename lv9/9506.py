import math

def calcFactorList(number):
  factorList = [1]
  loop = 2
  sqrtNum = math.sqrt(number)
  while loop <= sqrtNum:
    if number % loop == 0:
      factorList.append(loop)
      if loop != sqrtNum:
        factorList.append(int(number / loop))
    loop += 1
  return sorted(factorList)

num = int(input())
while num != -1:
  arr = calcFactorList(num)
  if sum(arr) != num:
    print(f'{num} is NOT perfect.')
  else:
    print(f'{num} = ', end='')
    for i in range(len(arr) - 1):
      print(f'{arr[i]} + ', end='')
    print(arr[-1])
  num = int(input())
