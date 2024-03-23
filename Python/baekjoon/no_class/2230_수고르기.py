n, m = map(int, input().split())
arr = sorted(list(int(input()) for _ in range(n)))
lt = 0
rt = 0
answer = int(2e9)

while lt <= rt < n:

    dif = arr[rt] - arr[lt]
    if dif < m:
        rt += 1
    else:
        answer = min(answer, dif)
        lt += 1
print(answer)

