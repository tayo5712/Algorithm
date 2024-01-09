def solution(land):
    n = len(land)
    DP = [[0 for _ in range(4)] for _ in range(n)]
    for i in range(4):
        DP[0][i] = land[0][i]
    
    # 리스트 슬라이싱으로 풀면 더 간단하게 풀 수 있음
    for i in range(1, n):
        for j in range(4):
            # 바로 윗 행만 아니면 됨
            if j == 0:
                DP[i][j] = max(DP[i-1][1], DP[i-1][2], DP[i-1][3]) + land[i][j]
            elif j == 1:
                DP[i][j] = max(DP[i-1][0], DP[i-1][2], DP[i-1][3]) + land[i][j]
            elif j == 2:
                DP[i][j] = max(DP[i-1][0], DP[i-1][1], DP[i-1][3]) + land[i][j]
            else:
                DP[i][j] = max(DP[i-1][1], DP[i-1][2], DP[i-1][0]) + land[i][j]
    
    return max(DP[n-1])
