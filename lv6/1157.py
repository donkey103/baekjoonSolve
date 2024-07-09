word = input()
word = word.upper()
cntList = [0]*26
for alpha in word:
  cntList[ord(alpha) - 65] += 1

maxValue = max(cntList)
maxIdxList = []
for i in range(len(cntList)):
  if cntList[i] == maxValue:
    maxIdxList.append(i)

if len(maxIdxList) == 1:
  print(chr(maxIdxList[0] + 65))
else: # len(maxIdxList) > 1
  print("?")
