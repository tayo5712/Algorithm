import sys
input = sys.stdin.readline

n = int(input())
D = [0] * (n+2)
day = [0] * (n+1)
pay = [0] * (n+1)

for i in range(1, n+1):
    day[i], pay[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i + day[i] - 1 > n:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], D[i+day[i]] + pay[i])

print(D[1])
