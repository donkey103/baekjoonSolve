n = int(input())
arr = list(map(int, input().split()))
maxScore = max(arr)
newArr = [i /maxScore * 100 for i in arr]
print(sum(newArr)/len(arr))