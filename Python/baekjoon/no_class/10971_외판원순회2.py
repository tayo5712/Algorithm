n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 1000000000


def travel(start, now, depth, cost):
    global answer
    if cost >= answer:
        return
    if depth >= n:
        if now == start:
            answer = min(answer, cost)
        return

    for i in range(n):
        if not visited[i] and arr[now][i]:  # 방문 하지 않았을 때랑 비용이 0이 아닐 때
            if i == start:
                if depth == n - 1:
                    visited[i] = 1
                    travel(start, i, depth + 1, cost + arr[now][i])
                    visited[i] = 0
            else:
                visited[i] = 1
                travel(start, i, depth + 1, cost + arr[now][i])
                visited[i] = 0


for i in range(n):
    visited = [0] * n
    travel(i, i, 0, 0)

print(answer)
