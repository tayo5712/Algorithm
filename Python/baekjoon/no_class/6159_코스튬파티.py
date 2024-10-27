import sys

input = sys.stdin.readline
n, s = map(int, input().split())
cnt = 0

cow = sorted([int(input()) for _ in range(n)])

start = 0
end = len(cow) - 1

while start < end:
    if cow[start] + cow[end] > s:
        end -= 1

    else:
        cnt += end - start
        start += 1

print(cnt)
