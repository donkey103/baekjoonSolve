a, b, c = map(int, input().split())

result = 0

if a == b == c:
  result = 10000 + a * 1000
elif a == b or b == c or c == a:
  if a == b or a == c:
    result = 1000 + a * 100
  else: # b == c
    result = 1000 + b * 100
else: # a != b != c
  result = max(a,b,c) * 100

print(result)