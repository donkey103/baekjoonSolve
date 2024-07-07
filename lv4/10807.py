total = int(input())
arrNum = list(map(int,input().split()))
target = int(input())
cnt = 0
for num in arrNum:
  if num == target:
    cnt += 1
print(cnt)