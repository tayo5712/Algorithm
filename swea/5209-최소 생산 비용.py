import sys
sys.stdin = open("input_5209.txt", "r")

def solve(row, sumV):   # 행, 합계
    global min_cost
    if row == n:        # 행을 다 돌면
        min_cost = min(min_cost, sumV)  # 최소값 비교
        return

    elif sumV >= min_cost:      # 지금까지 합한 값이 최소값보다 크면 리턴
        return

    for col in range(n):
        if not visited[col]:    # 방문한 열인지 체크
            visited[col] = 1    # 방문처리
            solve(row+1, sumV+cost[row][col])   # 행을 1 증가하고, 현재 합계 계산해서 넘겨줌
            visited[col] = 0    # 방문취소

for tc in range(1, int(input())+1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n+1)       # 열 방문 체크
    min_cost = 99 * n**2        # 나올 수 있는 최대값
    solve(0, 0)

    print(f'#{tc} {min_cost}')