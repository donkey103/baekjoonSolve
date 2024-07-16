arr = [[0 for _ in range(100)]  for _ in range(100)]

def attachPaper(x, y):
  for r in range(x, x+10):
    for c in range(y, y+ 10):
      arr[r][c] = 1

papers = int(input())
for _ in range(papers):
  x, y = map(int, input().split())
  attachPaper(x, y)

area = 0
for rowArr in arr:
  area += sum(rowArr)
print(area)