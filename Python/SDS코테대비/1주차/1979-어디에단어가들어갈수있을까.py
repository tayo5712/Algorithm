T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arrN = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+1)]
    arrR = list(zip(*arrN))     # 전치 행렬
    answer = 0
    for i in range(n+1):
        cntN = 0
        cntR = 0
        for j in range(n+1):
            if arrN[i][j] == 1:
                cntN += 1
            else:
                if cntN == k:
                    answer += 1
                cntN = 0

            if arrR[i][j] == 1:
                cntR += 1
            else:
                if cntR == k:
                    answer += 1
                cntR = 0
    print(f'#{tc} {answer}')

