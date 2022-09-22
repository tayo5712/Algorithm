import sys
input = sys.stdin.readline
N, K = map(int, input().split())
D = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    D[i][1] = i     # i개에서 1개 선택하는 경우의 수는 i개
    D[i][0] = 1     # i개에서 1개도 선택하지 않는 경우의 수는 1개
    D[i][i] = 1     # i개에서 i개 선택하는 경우의 수는 1개

for i in range(2, N+1):
    for j in range(1, i):   # 고르는 수의 개수가 전체 개수를 넘을 수 없음
        D[i][j] = D[i-1][j] + D[i-1][j-1]   # 조합 점화식

print(D[N][K])