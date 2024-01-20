from collections import deque

def solution(n, wires):
    answer = 10000
    
    def bfs(start, ban):
        visited = [0] * (n + 1)
        connect = 0
        q = deque()
        q.append(start)
        visited[start] = 1
        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if not visited[next_node] and node != ban:
                    connect += 1
                    visited[next_node] = 1
                    q.append(next_node)
        return abs((n - connect) - connect)
                
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    
    for wire in wires:
        answer = min(answer, bfs(wire[0], wire[1]))
    
    return answer
