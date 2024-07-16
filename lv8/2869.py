up, down, remain = map(int, input().split())
day = 1
if remain > up:
  day += (remain - up) // (up - down)
  day += 1 if (remain - up) % (up - down) > 0 else 0
else:
  day = 1

print(day)


