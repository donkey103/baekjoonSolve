def isPrime(num):
  if num == 1:
    return False
  elif num == 2:
    return True
  elif num % 2 == 0: # 2의 배수 전부 제거
    return False
  else: # 홀수 대상으로만 소수 판별
    sqrtNum = num ** (1/2)
    loops = 3
    while loops <= sqrtNum:
      if num % loops == 0:
        return False
      loops += 2
    return True

m = int(input())
n = int(input())
primeList = []
for i in range(m, n+1):
  if(isPrime(i)):
    primeList.append(i)

if len(primeList) == 0:
  print(-1)
else:
  print(sum(primeList))
  print(primeList[0])