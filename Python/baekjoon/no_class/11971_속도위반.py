n, m = map(int, input().split())
road = [0] * 100
yongjong = [0] * 100
st = 0
for i in range(n):
    r, s = map(int, input().split())
    for _ in range(r):
        road[st] = s
        st += 1
st = 0
for i in range(m):
    r, s = map(int, input().split())
    for _ in range(r):
        yongjong[st] = s
        st += 1
result = 0
for i in range(100):
    if yongjong[i] - road[i] > result:
        result = yongjong[i] - road[i]
print(result)
