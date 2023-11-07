from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
q = deque()
answer = []

for _ in range(m):
    arr = list(map(int, input().split()))
    if arr[0] > 1:
        for i in range(1, arr[0]):
            graph[arr[i]].append(arr[i+1])
            inDegree[arr[i+1]] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for node in graph[tmp]:
        inDegree[node] -= 1
        if inDegree[node] == 0:
            q.append(node)

if len(answer) == n:
    for i in range(n):
        print(answer[i])
else:
    print(0)

