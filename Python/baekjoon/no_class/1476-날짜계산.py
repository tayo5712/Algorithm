e, s, m = map(int, input().split())
es, ss, ms, cnt = 1, 1, 1, 1
while True:
    if e == es and s == ss and m == ms:
        break
    else:
        es += 1
        ss += 1
        ms += 1
        cnt += 1
    if es > 15:
        es -= 15
    if ss > 28:
        ss -= 28
    if ms > 19:
        ms -= 19
print(cnt)
