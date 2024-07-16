def checkGroupWord(word):
  prevCharList = []
  for alpha in word:
    if alpha not in prevCharList:
      prevCharList.append(alpha)
    elif alpha == prevCharList[-1]: # 직전에 추가된 문자와 같으면 연속 문자로 취급
      continue
    else: # 직전에 추가되지 않은 문자가 다시 나오면 그룹 단어가 아님
      return False 
  return True

num = int(input())
grouptWordCnt = 0
for _ in range(num):
  word = input()
  if checkGroupWord(word):
    grouptWordCnt += 1
print(grouptWordCnt)