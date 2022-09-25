import sys
input = sys.stdin.readline

D = [[0] * 30 for _ in range(30)]

for i in range(30):
    D[i][1] = i     # i개에서 1개 선택하는 경우의 수는 i개
    D[i][0] = 1     # i개에서 1개도 선택하지 않는 경우의 수는 1개
    D[i][i] = 1     # i개에서 i개 선택하는 경우의 수는 1개

for i in range(2, 30):
    for j in range(1, i):   # 고르는 수의 개수가 전체 개수를 넘을 수 없음
        D[i][j] = D[i-1][j] + D[i-1][j-1]   # 조합 점화식

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(D[m][n])
