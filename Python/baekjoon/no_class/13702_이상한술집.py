import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))

left = 1
right = max(arr)
answer= 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for mak in arr:
        cnt += mak // mid
    if cnt >= k:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)
