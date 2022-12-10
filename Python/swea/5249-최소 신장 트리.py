import sys
sys.stdin = open("input_5249.txt", "r")

def prim():         # prim 알고리즘
    check = []
    value = [100000] * (v+1)
    value[0] = 0
    for _ in range(v):         # 현재 최소 가중치를 갖는 노드를 찾음
        minV = 100000
        for i in range(v+1):
            if i not in check and minV > value[i]:
                minV = value[i]
                curV = i

        check.append(curV)      # 방문 처리

        for j in range(v+1):    # 가중치가 더 적은 걸로 바꿔 줌
            if j not in check and tree[curV][j] and value[j] > tree[curV][j]:
                value[j] = tree[curV][j]

    return sum(value)

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    tree = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        st, ed, w = map(int, input().split())
        tree[st][ed] = w
        tree[ed][st] = w

    print(f'#{tc} {prim()}')

