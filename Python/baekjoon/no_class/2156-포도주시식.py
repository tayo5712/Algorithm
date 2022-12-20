n = int(input())
wine = [int(input()) for _ in range(n)]
d = [0]*n
if n == 1:  # 포도주 개수가 1개 일 때
    d[0] = wine[0]
else:
    d[1] = wine[0] + wine[1]    # 포도주 개수가 2개 일 때
    d[2] = max(wine[2] + wine[1], wine[2] + d[0], d[1])     # 포도주 개수가 3개 일 때
    for i in range(3, n):
        d[i] = max(d[i-1], d[i-3] + wine[i-1] + wine[i], d[i-2] + wine[i])
        # 현재 포도주를 마시지 않을 때
        # 현재 포도주와 전 포도주를 마시고 전전 포도주를 마시지 않을 때
        # 현재 포도주와 전전 포도주를 마시고 전 포도주를 마시지 않을 때

print(d[n-1])