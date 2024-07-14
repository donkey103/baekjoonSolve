arr = []
for _ in range(5):
  arr.append(input())

for r in range(15):
  for c in range(5):
    if r < len(arr[c]):
      print(arr[c][r], end='')
    else:
      continue
