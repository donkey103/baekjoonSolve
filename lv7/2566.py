arr = []
for _ in range(9):
  arr.append(list(map(int, input().split())))

max = -1
rowIndex = -1
colIndex = -1
for ri in range(9):
  for ci in range(9):
    if arr[ri][ci] > max:
      max = arr[ri][ci]
      rowIndex = ri
      colIndex = ci
print(max)
print(f'{rowIndex + 1} {colIndex + 1}')