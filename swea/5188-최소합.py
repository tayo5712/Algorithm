import sys

sys.stdin = open("input_5188.txt", "r")

def dfs(i, j, sumV):
    global minV
    if i == n-1 and j == n-1:   # 오른쪽 아래 끝에 도착하면
        minV = min(minV, sumV)  # 최소합 비교
        return

    if sumV >= minV:    # 현재까지 더한 값이 최소합 보다 크면 리턴
        return

    for di, dj in ((0, 1), (1, 0)):     # 왼쪽 위에서 오른쪽 아래까지 가므로 (아래, 오른쪽)으로만 움직일 수 있다.
        ni = i + di
        nj = j + dj
        if ni < n and nj < n :      # 범위 안이면
            dfs(ni, nj, sumV+arr[ni][nj])   # 다음 칸의 좌표와 현재 칸의 값을 sumV에 더해서 넘겨준다.

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minV = 1000
    dfs(0, 0, arr[0][0])    # 맨 처음 시작점은 (0,0) 이고 (0,0) 에 해당하는 값을 sumV의 초기값으로 설정
    print(f'#{tc} {minV}')
