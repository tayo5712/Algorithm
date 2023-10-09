import itertools

def dfs(count, win, draw, loss):
    if count == 15:
        global ans
        if win.count(0) == 6 and draw.count(0) == 6 and loss.count(0) == 6:
            ans = 1
        return

    home, away = match[count]
    if win[home] > 0 and loss[away] > 0:
        win[home] -= 1
        loss[away] -= 1
        dfs(count + 1, win, draw, loss)
        win[home] += 1
        loss[away] += 1
    if draw[home] > 0 and draw[away] > 0:
        draw[home] -= 1
        draw[away] -= 1
        dfs(count + 1, win, draw, loss)
        draw[home] += 1
        draw[away] += 1
    if loss[home] > 0 and win[away] > 0:
        loss[home] -= 1
        win[away] -= 1
        dfs(count + 1, win, draw, loss)
        loss[home] += 1
        win[away] += 1

records = [[0 for _ in range(3)] for _ in range(6)]
match = list(itertools.combinations(range(6), 2))
ans = 0
for i in range(4):
    win, draw, loss = [], [], []
    result = list(map(int, input().split()))
    for j in range(0, 16, 3):
        win.append(result[j])
        draw.append(result[j + 1])
        loss.append(result[j + 2])
    ans = 0
    dfs(0, win, draw, loss)
    print(ans, end=" ")


