import sys

sys.stdin = open("input_5189.txt", "r")

def solve(st, cnt, sumV):
    global minV
    if cnt == n:    # 이동횟수가 관리구역의 넓이와 같아지면
        minV = min(minV, sumV+arr[st][0])   # 최소 배터리 총 사용량 비교
        return                              # 마지막에 도착해서 도착점 배터리량을 더해줌

    # 현재 위치가 (x,y) 라면 다음 위치는 무조건 (y,?)가 되어야함
    for k in range(1, n):   # 0은 출발점이므로 중간에 돌아와서는 안되기 때문에 0은 제외
        if k != st and not visited[k]:  # 좌표값의 (x,y)값이 같으면 다음 칸으로 갈 수 없음
            visited[k] = 1     # 방문 처리
            solve(k, cnt+1, sumV+arr[st][k])    # 현재 칸의 y좌표를 다음칸의 x좌표로 넣어주고, 이동 횟수를 추가하고, 현재 칸의 배터리 사용량을 더해서 넘겨준다.
            visited[k] = 0     # 방문 취소

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n   # 방문 여부
    minV = 100000       # 최소값
    solve(0, 1, 0)      # 시작점, 이동횟수, 배터리 총 사용량
    print(f'#{tc} {minV}')

