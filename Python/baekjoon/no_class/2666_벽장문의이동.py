n = int(input())
open1, open2 = map(int, input().split())
m = int(input())
order = list(int(input()) for _ in range(m))
answer = int(1e4)

def dfs(o1, o2, depth, cnt):
    global answer
    if cnt >= answer:
        return
    if depth == m:
        answer = cnt
        return
    else:
        distance1 = abs(o1 - order[depth])
        distance2 = abs(o2 - order[depth])
        dfs(order[depth], o2, depth + 1, cnt + distance1)
        dfs(o1, order[depth], depth + 1, cnt + distance2)
        
dfs(open1, open2, 0, 0)
print(answer)
