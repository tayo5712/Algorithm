N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
answer = 0
cur = 0 # 웅덩이를 덮은 마지막 널빤지의 위치
for start, end in arr:
    if cur > start:
        start = cur
    while start < end:
        start += L
        answer += 1
    cur = start
print(answer)
