fullSet = [1, 1, 2, 2, 2, 8]
inputSet = list(map(int, input().split()))
resultSet = []
for i in range(len(fullSet)):
  resultSet.append(fullSet[i] - inputSet[i])

for el in resultSet:
  print(el, end=' ')