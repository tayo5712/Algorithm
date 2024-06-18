N, K = map(int, input().split())
arr = list(map(int, input().split()))
diff = [0] * (N - 1)
for i in range(N - 1):
    diff[i] = arr[i + 1] - arr[i]

print(sum(sorted(diff)[:N-K]))
