n = int(input())
cnt = 1
t = 0
while n > 0:
    if cnt <= n:
        t += 1
        n -= cnt
        cnt += 1
    else:
        cnt = 1
print(t)
