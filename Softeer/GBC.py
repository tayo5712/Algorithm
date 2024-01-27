import sys

input = sys.stdin.readline

n, m = map(int, input().split())
limits = [0] * 101
tests = [0] * 101
answer = 0

index = 1
for _ in range(n):
    a, v = map(int, input().split())
    for i in range(index, index + a):
        limits[i] = v
    index += a
    
index = 1
for _ in range(m):
    a, v = map(int, input().split())
    for i in range(index, index + a):
        tests[i] = v
    index += a
    
for i in range(1, 101):
    if tests[i] > limits[i]:
        answer = max(answer, tests[i] - limits[i])

print(answer)
