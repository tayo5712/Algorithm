import sys
sys.stdin = open("input_1795.txt", "r")

from queue import PriorityQueue

def dik(s, tree):
    check = []
    value = [1000000] * (n+1)
    q = PriorityQueue()
    value[s] = 0
    q.put((value[s], s))
    while len(check) < n:
        w, curV = q.get()
        if curV not in check:
            check.append(curV)
            for i in range(n+1):
                if i not in check and tree[curV][i] and value[i] > value[curV] + tree[curV][i]:
                    value[i] = value[curV] + tree[curV][i]
                    q.put((value[i], i))
    return value

T = int(input())
for tc in range(1, T+1):
    n, m, start = map(int, input().split())
    tree1 = [[0] * (n+1) for _ in range(n+1)]
    tree2 = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        st, ed, w = map(int, input().split())
        tree1[st][ed] = w
        tree2[ed][st] = w

    outV = dik(start, tree1)    # 진출 최소값
    inV = dik(start, tree2)     # 진입 최소값

    answer = 0
    for i in range(1, n+1):
        answer = max(answer, outV[i] + inV[i])

    print(f'#{tc} {answer}')


