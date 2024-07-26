n, m = map(int, input().split())
arr = list(range(1, n + 1))
for _ in range(m):
    a, b = map(lambda x : int(x) - 1, input().split())
    arr = arr[:a] + arr[a:b+1][::-1] + arr[b + 1:]
print(*arr)
