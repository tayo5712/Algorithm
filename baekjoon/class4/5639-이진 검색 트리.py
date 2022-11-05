import sys
sys.setrecursionlimit(10**6)

def dfs(st, ed):
    if st > ed:
        return
    mid = ed+1  # 자식 노드 중에 부모 노드보다 큰 값이 없는  경우 st > ed로 return되게 만들려고
    for i in range(st+1, ed+1):
        if graph[st] < graph[i]:
            mid = i
            break

    # 전위 순회 ( 부모가 나중에 출력 )
    dfs(st+1, mid-1)    # 왼쪽 트리
    dfs(mid, ed)    # 오른쪽 트리
    print(graph[st])

graph = []

while True:
    try:
        graph.append(int(input()))
    except:
        break

dfs(0, len(graph)-1)