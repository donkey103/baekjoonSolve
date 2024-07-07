arr = []
for _ in range(10):
  num = int(input())
  arr.append(num % 42)

distinctArr = set(arr)
print(len(distinctArr))

