loop = int(input())
for i in range(1, loop+1):
  print(' ' * (loop - i), end='')
  print('*' * i, end='')
  print()
  