# 개념
# 1. 입력값 N 받기, counter=0
# 2. 0 부터 시작
# 3. 숫자를 계속 올려나간다
# 4. 숫자를 문자열로 변환하고 '666'이 포함되어 있는지 확인
# 5. 포함되면 counter를 +1 올리고 입력값과 동일한지 확인
# 6. 동일하면 숫자를 출력하고 break

import sys
N = int(sys.stdin.readline())
counter = 0
num = 0

while counter < N:
  num += 1
  if '666' in str(num):
    counter += 1

# counter == N
print(num)
