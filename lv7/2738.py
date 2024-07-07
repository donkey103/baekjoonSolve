n, m = map(int, input().split())
a = []
b = []
for i in range(n * 2):
  row = list(map(int, input().split()))
  if i < n:
    a.append(row)
  else:
    b.append(row)
print(a)
print(b)
c = [[0 for _ in range(m)] for _ in range(n)]
for row in range(n):
  for col in range(m):
    c[row][col] = a[row][col] + b[row][col]
print(c)

for row in range(n):
  for col in range(m):
    print(c[row][col], end=' ')
  print()