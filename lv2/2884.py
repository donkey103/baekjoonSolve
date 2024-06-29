hour, min = map(int, input().split())

min -= 45
if min < 0:
  hour -= 1
  min += 60

if hour < 0:
  hour += 24

print(f'{hour} {min}')