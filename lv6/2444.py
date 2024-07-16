n = int(input())

for i in range(1, 2*n):
  absMod = abs(i - n) % n
  print(' '* absMod + '*' * (2 * (n - absMod) - 1))