a = int(input())
b = int(input())

r3 = (b // 1 % 10) * a
r4 = (b // 10 % 10) * a
r5 = (b // 100 % 10) * a
r6 = a * b

print(r3)
print(r4)
print(r5)
print(r6)
