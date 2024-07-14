l = [0] * 16 # 한변의 점의 개수
l[0] = 2

n = int(input())
for i in range(1, n + 1):
  l[i] = 2 * l[i - 1] - 1

print( l[n] ** 2)

