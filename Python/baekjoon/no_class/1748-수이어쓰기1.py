n = int(input())
origin = n
cnt = 0
i = 1
num = 1
while (n - (9*i)) >= 0:
    cnt += 9 * i * num
    num += 1
    n -= 9 * i
    i *= 10
cnt += (origin - i + 1) * num
print(cnt)