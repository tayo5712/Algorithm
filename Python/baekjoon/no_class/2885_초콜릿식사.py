k = int(input())
n, cnt = 1, 0
while n < k:
    n *= 2
if n == k:
    print(n, 0)
else:
    ans = n
    while (k > 0):
        if k >= n:
            k -= n
        else:
            n //= 2
            cnt += 1
    print(ans, cnt)
