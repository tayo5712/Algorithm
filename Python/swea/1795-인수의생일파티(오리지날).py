def dik(s, tree):
    check = []
    value = [1000000] * (n + 1)
    value[s] = 0
    for _ in range(n):
        minV = 10000000
        for i in range(n + 1):
            if i not in check and minV > value[i]:
                minV = value[i]
                curV = i
        check.append(curV)
        for j in range(n + 1):
            if j not in check and tree[curV][j] and value[j] > value[curV] + tree[curV][j]:
                value[j] = value[curV] + tree[curV][j]
    return value[1:]


T = int(input())
for tc in range(1, T + 1):
    n, m, start = map(int, input().split())
    tree1 = [[0] * (n + 1) for _ in range(n + 1)]
    tree2 = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        st, ed, w = map(int, input().split())
        tree1[st][ed] = w
        tree2[ed][st] = w

    outV = dik(start, tree1)  # 진출 최소값
    inV = dik(start, tree2)  # 진입 최소값

    answer = 0
    for i in range(n):
        answer = max(answer, outV[i] + inV[i])

    print(f'#{tc} {answer}')