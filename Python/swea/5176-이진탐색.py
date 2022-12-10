import sys

sys.stdin = open("input_5176.txt", "r")

def inorder(node):  # 중위 순회 실시
    global cnt

    if node <= n:
        inorder(node*2)
        tree[node] = cnt
        cnt += 1
        inorder(node*2+1)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    tree = [[0] for _ in range(n+1)]

    cnt = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')