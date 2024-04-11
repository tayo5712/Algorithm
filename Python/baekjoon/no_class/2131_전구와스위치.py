n = int(input())
target = list(map(int, input()))
goal = list(map(int, input()))
ans = 1e9

def turn(light):
    cnt = 0
    for i in range(1, n):
        if light[i - 1] != goal[i - 1]:
            light[i - 1] = 1 - light[i - 1]
            light[i] = 1 - light[i]
            if i < n - 1:
                light[i + 1] = 1 - light[i + 1]
            cnt += 1
    return cnt if light == goal else 1e9

# 첫 번째 전구를 누르지 않았을 때
ans = turn(target[:])

# 첫 번째 전구를 누를 때
target[0] = 1 - target[0]
target[1] = 1 - target[1]
ans = min(ans, turn(target) + 1)

print(ans) if ans != 1e9 else print(-1)
