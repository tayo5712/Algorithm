n, k = map(int, input().split())
arr = list(map(int, input().split()))

e, answer, tmp, odd = 0, 0, 0, 0

for s in range(n):
    while odd <= k and e < n:
        if arr[e] % 2:
            odd += 1
        else:
            tmp += 1
        e += 1

        if s == 0 and e == n:
            answer = tmp
            break
    if odd == k + 1:
        answer = max(tmp, answer)
    if arr[s] % 2:
        odd -= 1
    else:
        tmp -= 1
print(answer)
