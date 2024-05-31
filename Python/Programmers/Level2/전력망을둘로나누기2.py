from collections import deque

answer = 100
def solution(n, wires):

    def bfs(start, ban):
        global answer
        visited = [0 for _ in range(n + 1)]
        connect = 1
        q = deque()
        visited[start] = 1
        q.append(start)
        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if not visited[next_node] and next_node != ban:
                    visited[next_node] = 1
                    connect += 1
                    q.append(next_node)
        answer = min(answer, abs(connect - (n - connect)))

    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    for wire in wires:
        bfs(wire[0], wire[1])

    return answer
