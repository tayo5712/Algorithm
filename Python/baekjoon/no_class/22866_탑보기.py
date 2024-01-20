# 현재 건물의 높이보다 높은 건물만 볼 수 있음

n = int(input())
arr = list(map(int, input().split()))
result = [0] * n
INF = int(1e5)
close = [INF] * n
l_stack = []

for i in range(n):
    if len(l_stack):
        while l_stack and l_stack[-1][1] <= arr[i]:
            l_stack.pop()
        result[i] += len(l_stack)
        if l_stack:
            close[i] = l_stack[-1][0]
    l_stack.append((i, arr[i]))

r_stack = []
for i in range(n-1, -1, -1):
    if len(r_stack):
        while r_stack and r_stack[-1][1] <= arr[i]:
            r_stack.pop()
        result[i] += len(r_stack)
        if r_stack:
            if close[i] == INF:
                close[i] = r_stack[-1][0]
            else:
                if i - close[i] > r_stack[-1][0] - i:
                    close[i] = r_stack[-1][0]
    r_stack.append((i, arr[i]))

for i in range(n):
    if result[i]:
        print(result[i], close[i] + 1)
    else:
        print(0)
