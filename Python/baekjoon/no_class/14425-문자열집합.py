import sys
input = sys.stdin.readline
n, m = map(int, input().split())
group = set(input().rstrip() for _ in range(n))
cnt = 0
for _ in range(m):
    word = input().rstrip()
    if word in group:
        cnt += 1
print(cnt)