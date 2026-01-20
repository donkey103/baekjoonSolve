N = int(input())

fiveBags = N // 5
fiveRemains = N % 5
threeBags = 0
threeRemains = 0

while fiveBags >= 0:
	threeRemains = fiveRemains % 3

	if threeRemains == 0:
		break

	fiveBags -= 1
	fiveRemains += 5

if fiveBags < 0:
	print(-1)
else:
	threeBags = fiveRemains // 3
	print(fiveBags + threeBags)