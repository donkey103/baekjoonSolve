loops = int(input())
for _ in range(loops):
  num, word = input().split()
  num = int(num)

  newWord = []
  for chara in word:
    newWord.append(chara * num)
  print("".join(newWord))
