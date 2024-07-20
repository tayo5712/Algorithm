from itertools import combinations

n, m = map(int, input().split())
nomat = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    nomat[a-1][b-1] = True
    nomat[b-1][a-1] = True

answer = 0
for com in combinations(range(n), 3):
    if nomat[com[0]][com[1]] or nomat[com[0]][com[2]] or nomat[com[1]][com[2]]:
        continue
    answer += 1
print(answer)
