tc = int(input())
answer = 0
def dfs(p, score):
    global max_score
    if p == 11:
        max_score = max(max_score, score)
        return
    for i in range(11):
        if not position[i] and player[p][i]:
            position[i] = 1
            dfs(p+1, score+player[p][i])
            position[i] = 0

for _ in range(tc):
    player = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    position = [0] * 11
    dfs(0, 0)
    print(max_score)
