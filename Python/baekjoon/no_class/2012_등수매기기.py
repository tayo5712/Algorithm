n = int(input())
arr = list(int(input()) for _ in range(n))
arr.sort()
result = 0
for i in range(1, n + 1):
    result += abs(arr[i-1] - i)
print(result)