def solution(n, computers):
    answer = 0    
    graph = [[] for _ in range(n)]
    
    def dfs(node):
        for v in graph[node]:
            if not visited[v]:
                visited[v] = 1
                dfs(v)
        return
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].append(j)
    
    print(graph)
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    
    return answer
