def solve(total):
    idx, sqr = 0, 1
    while sqr <= total:
        sqr *= 2
        idx += 1
    return idx, sqr // 2


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    if X >= 2 ** (N - 1):
        ans = [- 1]
    else:
        ans = [i for i in range(1, N + 1)]
        while X:
            idx, tot = solve(X)
            ans[0], ans[idx] = ans[idx], ans[0]
            X -= tot
    print(f"#{tc}", end=" ")
    for a in ans:
        print(a, end=" ")
    print()