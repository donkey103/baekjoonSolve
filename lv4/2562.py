arr = []
for i in range(9):
  arr.append(int(input()))

maxNum = 0
maxIdx = -1
for idx in range(9):
  if arr[idx] >= maxNum:
    maxNum = arr[idx]
    maxIdx = idx

print(maxNum)
print(maxIdx + 1)