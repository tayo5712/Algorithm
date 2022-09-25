import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
D = [[0] * 202 for _ in range(202)]

# 조합 테이블 미리 만들어 놓기
for i in range(201):
    for j in range(i+1):    # 고르는 수의 개수가 전체 개수를 넘을 수 없음
        if j == 0 or j == i:
            D[i][j] = 1

        else:
            D[i][j] = D[i-1][j] + D[i-1][j-1]   # 조합 점화식
            # if D[i][j] > 1000000000:             # k의 범위를 벗어나면 범위의 최댓값 저장
            #     D[i][j] = 1000000001

if D[n+m][m] < k:   # 주어진 자릿수로 만들 수 없는 k번째 수의 경우
    print(-1)

else:
    while not (n == 0 and m == 0):
        if D[n-1+m][m] >= k:    # if a 문자를 선택했을 때 남은 문자들로 만들 수 있는 모든 경우의 수 >= k
            print('a', end='')
            n -= 1
        else:
            print('z', end='')
            k -= D[n-1+m][m]    # k의 값을 모든 경우의 수를 뺀 값으로 저장
            m -= 1  # z 문자 개수 감소