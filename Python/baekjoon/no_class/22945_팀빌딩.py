n = int(input())
team = list(map(int, input().split()))

st = 0
ed = n - 1
maxV = 0
while st + 1 < ed:
    power = (ed - st - 1) * min(team[st], team[ed])
    maxV = max(maxV, power)
    if team[st] < team[ed]:
        st += 1
    else:
        ed -= 1
print(maxV)
