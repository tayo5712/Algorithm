import sys

sys.stdin = open("input_5178.txt", "r")

# def node_sum(L):
#     if L > N:
#         return 0
#     if node[L]:
#         return node[L]
#     else:
#         return node_sum(L*2) + node_sum(L*2+1)

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    node = [0 for i in range(N + 1)]
    for i in range(M):
        n, v = map(int, input().split())
        node[n] = v

    for j in range(N, 1, -1):       # 부모 노드에 자식 노드에 들어 있는 값을 더해 줌
        node[j//2] += node[j]

    print(f'#{tc} {node[L]}')