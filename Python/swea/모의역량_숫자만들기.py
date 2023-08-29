def cal(left, right, oper):
    if oper == 0:
        return left + right
    elif oper == 1:
        return left - right
    elif oper == 2:
        return left * right
    else:
        return int(left / right)

def dfs(left, depth):
    global minV, maxV
    if depth == n:
        minV = min(minV, left)
        maxV = max(maxV, left)
    for i in range(4):
        if opers[i] != 0:
            opers[i] -= 1
            dfs(cal(left, numbers[depth], i), depth + 1)
            opers[i] += 1

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    minV = 100000001
    maxV = -100000001
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    dfs(numbers[0], 1)
    print(f'#{tc} {maxV-minV}')