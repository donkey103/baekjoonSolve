n, k = map(int, input().split())
xlist = list(map(int, input().split()))
xlist.sort()
xlist.reverse()
print(xlist[k-1])
