import sys
sys.stdin = open("input_4012.txt", "r")

def dfs(i, k):
    global result
    if i == n // 2:  # 한 음식에 선택 되는 재료의 개수가 되면 (n//2)
        a = []
        b = []
        for j in range(n):
            if visit[j]:  # 방문 한 곳 이면 a에 저장
                a.append(j)
            else:   # 아니면 b에 저장
                b.append(j)
        a_s = 0
        b_s = 0
        for i in range(n // 2):         # 음식의 시너지 구하기
            for j in range(i + 1, n // 2):
                a_s += recipe[a[i]][a[j]] + recipe[a[j]][a[i]]
                b_s += recipe[b[i]][b[j]] + recipe[b[j]][b[i]]

        if abs(a_s - b_s) < result: # 최소값 비교
            result = abs(a_s - b_s)
        return

    for j in range(k, n):   # 조합
        if not visit[j]:
            visit[j] = 1
            dfs(i + 1, j + 1)
            visit[j] = 0

for tc in range(1, int(input()) + 1):
    n = int(input())
    visit = [0] * n
    recipe = [list(map(int, input().split())) for _ in range(n)]
    result = 10000000

    dfs(0, 0)
    print(f'#{tc} {result}')

