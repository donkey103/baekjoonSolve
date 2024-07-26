# 두번 나온 좌표를 제외한 숫자가 추가해야 할 x, y
xList = []
yList = []

def setList(list: list, num: int) -> None:
  if num in list:
    list.remove(num)
  else:
    list.append(num)

for _ in range(3):
  x, y = map(int, input().split())
  setList(xList, x)
  setList(yList, y)

print(f'{xList[0]} {yList[0]}')