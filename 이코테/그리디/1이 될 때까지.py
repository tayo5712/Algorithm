N, K = map(int, input().split())
cnt = 0
# while N > 1:
#     if N % K == 0:
#         N = N // K
#         cnt += 1
#     else:
#         N = N - 1
#         cnt += 1
#
# print(cnt)

while True:
    target = (N // K) * K
    cnt += (N - target)
    N = target
    if N < K:
        break
    cnt += 1
    N //= K

cnt += (N - 1)
print(cnt)