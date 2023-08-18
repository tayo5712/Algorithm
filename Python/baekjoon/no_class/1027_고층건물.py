n = int(input())
buildings = list(map(int, input().split()))
answer = 0
for i in range(n):
    sight = 0
    pre = 1000000000
    for left in range(i-1, -1, -1):
        m = (buildings[i] - buildings[left]) / (i - left)
        if pre > m:
            pre = m
            sight += 1
    pre = -1000000000
    for right in range(i+1, n):
        m = (buildings[i] - buildings[right]) / (i - right)
        if pre < m:
            pre = m
            sight += 1
    answer = max(answer, sight)
print(answer)