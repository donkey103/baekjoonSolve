x = int(input())

# 몇번째 줄에 포함되는지 확인
row = 0
while x > row*(row+1)/2:
  row += 1
# 해당 row의 몇번째 숫자인지 계산
nth = x - (row-1)*row/2
if row % 2 == 0:
  print(f'{int(nth)}/{int(row + 1 - nth)}')
else:
  print(f'{int(row + 1 - nth)}/{int(nth)}')

