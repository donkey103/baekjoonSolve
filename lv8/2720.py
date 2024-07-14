currents = [25, 10, 5, 1]

def printCoins(change):
  for i in range(len(currents)):
    units = change // currents[i]
    change -= units * currents[i]
    print(units, end=' ')


cases = int(input())
for _ in range(cases):
  printCoins(int(input()))