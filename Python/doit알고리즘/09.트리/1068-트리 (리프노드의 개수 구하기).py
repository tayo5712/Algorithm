import sys

input = sys.stdin.readline
n = int(input())
visited = [0] * n
tree = [[] for _ in range(n)]
tree_list = list(map(int, input().split()))
deletenode = int(input())
answer = 0

for i in range(n):
    if tree_list[i] != -1:
        tree[i].append(tree_list[i])
        tree[tree_list[i]].append(i)
    else:
        root = i        # -1이면 해당 인덱스는 루트 노드

def dfs(v):
    global answer
    visited[v] = 1
    child_node = 0              # 자식 개수
    for k in tree[v]:
        if not visited[k] and k != deletenode:      # 삭제노드 이면 탐색 중지
            child_node += 1     # 자식 개수 증가
            dfs(k)

    if not child_node:  # 해당 노드에 자식이 없으면
        answer += 1     # 답에 1 증가

if deletenode == root:      # 삭제 노드값이 루트노드이면 리프노드 0개
    print(0)

else:
    dfs(root)
    print(answer)

