from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def dijk(st):
        result = 0
        heap = []
        INF = int(1e9)
        distance = [INF] * (N + 1)
        distance[st] = 0
        heappush(heap, (0, st))
        while heap:
            dist, now_node = heappop(heap)

            for next_node, next_dist in graph[now_node]:
                cost = distance[now_node] + next_dist # 다음 노드로 가는 비용
                if distance[next_node] > cost:
                    distance[next_node] = cost
                    heappush(heap, (cost, next_node))

        # K 이하의 개수
        for i in range(1, N + 1):
            if distance[i] <= K:
                result += 1
        return result
    answer = dijk(1)
    
    return answer
