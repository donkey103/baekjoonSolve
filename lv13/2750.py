n = int(input())
lst = []
for _ in range(n):
  lst.append(int(input()))

for i in range(len(lst) - 1):
  for j in range(0, len(lst) - i - 1):
    if lst[j] > lst[j + 1]:
      lst[j], lst[j + 1] = lst[j + 1], lst[j]

for el in lst:
  print(el)
