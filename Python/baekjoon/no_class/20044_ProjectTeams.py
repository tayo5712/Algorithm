n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = arr[0] + arr[-1]
for i in range(1, n):
    answer = min(answer, arr[i] + arr[-(i+1)])
print(answer)