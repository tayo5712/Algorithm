import sys
sys.stdin = open("input_5251.txt", "r")

def dik():
    curV = 0
    check = []
    value = [1000000] * (v+1)
    value[0] = 0
    for _ in range(v):
        minV = 1000000
        for i in range(v+1):
            if i not in check and minV > value[i]:      # 현재 최소 가중치를 갖는 노드를 찾는다.
                minV = value[i]
                curV = i

        check.append(curV)

        for j in range(v+1):            # 현재 노드까지의 가중치와 다음 노드까지의 가중치를 더해서 다음 노드의 값과 최소 비교
            if j not in check and tree[curV][j] and value[j] > value[curV] + tree[curV][j]:
                value[j] = value[curV] + tree[curV][j]

    return value[-1]

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    tree = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        st, ed, w = map(int, input().split())
        tree[st][ed] = w    # 방향 그래프

    print(f'#{tc} {dik()}')
