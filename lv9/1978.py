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

numbers = int(input())
targets = list(map(int, input().split()))
cnt = 0
for i in range(numbers):
  if isPrime(targets[i]):
    cnt += 1
print(cnt)

