import sys

sys.stdin = open("input_5174.txt", "r")

def preorder(n):        # 노드 n에서 순회시작
    global cnt
    if n:
        cnt += 1        # 노드 방문마다 cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))

    ch1 = [0] * (e+2)
    ch2 = [0] * (e+2)
    for i in range(0, e*2, 2):
        p, c = nodes[i], nodes[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    preorder(n)
    print(f'#{tc} {cnt}')

