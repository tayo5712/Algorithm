from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for com in combinations(range(m), 3):
    maxV = 0
    for i in range(n):
        maxV += max(arr[i][com[0]], arr[i][com[1]], arr[i][com[2]])
    answer = max(answer, maxV)
print(answer)
