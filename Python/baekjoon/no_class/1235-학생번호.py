n = int(input())
arr = list(input() for _ in range(n))
m = len(arr[0])
k = 1
while True:
    result = set()
    for i in range(n):
        result.add(arr[i][m-k:])
    if len(result) == n:
        break
    k += 1
print(k)
