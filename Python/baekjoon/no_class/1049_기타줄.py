N, M = map(int, input().split())
pack = []
single = []
for _ in range(M):
    a, b = map(int, input().split())
    pack.append(a)
    single.append(b)

min_pack = min(pack)
min_single = min(single)
result = 0

if min_pack <= 6 * min_single:
    if min_pack < min_single * (N % 6):
        result = min_pack * (N // 6 + 1)
    else:
        result = min_pack * (N // 6) + min_single * (N % 6)
else:
    result = min_single * N

print(result)