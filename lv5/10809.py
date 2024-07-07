arr = [-1]*26
word = input()
print(chr(122))
for i in range(97, 124): # a ~ z
  if chr(i) in word:
    arr[i-97] = word.index(chr(i))

for el in arr:
  print(el, end=' ')