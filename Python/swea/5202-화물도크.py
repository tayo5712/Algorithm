import sys

sys.stdin = open("input_5202.txt", "r")

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[1])     # 끝나는 시간을 기준으로 정렬
    result = 1
    ed = arr[0][1]      # 제일 첫 번째 화물이 끝나는 시간을 초기값으로 잡음
    for i in range(1, n):
        if arr[i][0] >= ed:    # 앞의 화물의 끝나는 시간이 현재 화물의 시작시간 보다 작으면
            result += 1        # 화물차 개수 추가
            ed = arr[i][1]     # ed를 현재 화물의 끝나는 시간으로 바꿔준다.

    print(f'#{tc} {result}')
