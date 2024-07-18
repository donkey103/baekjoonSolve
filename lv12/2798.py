n, m = map(int, input().split())
numbers = list(map(int, input().split()))

maxSum = 0
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum = numbers[i] + numbers[j] + numbers[k]
      if maxSum < sum <= m:
        maxSum = sum
print(maxSum)
