dial = ["", "", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", ""]
word = input()
sum = 0
for character in word:
  for idx in range(len(dial)):
    if character in dial[idx]:
      sum += idx
      break
print(sum)
