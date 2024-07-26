x, y, w, h = map(int, input().split())

top = h - y
bottom = y
left = x
right = w - x

print(min(top, bottom, left, right))