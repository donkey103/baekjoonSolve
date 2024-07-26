arr = list(map(int, input().split()))

total = sum(arr)
maxLen = max(arr)

if maxLen < (total - maxLen):
  print(total)
else: # maxLen >= (total - maxLen)
  newMaxLen = (total - maxLen) -1
  print(total - maxLen + newMaxLen)

