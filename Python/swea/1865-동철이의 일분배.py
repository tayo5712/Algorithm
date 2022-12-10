import sys
sys.stdin = open("input_1865.txt", "r")

def per(row, now_per):
    global max_per

    if row == n:
        max_per = max(max_per, now_per)
        return

    elif now_per <= max_per:    # 1보다 작은 소수이기 때문에 곱할 수록 값이 작아지기 때문에 현재값이 최대값 보다 작은면 현재값은 계속 곱해져서 작아지기 때문에 볼필요가 없다.
        return

    else:
        for col in range(n):
            if not visited[col]:
                visited[col] = 1
                per(row + 1, now_per * arr[row][col])   # 곱한 값을 넘겨줌
                visited[col] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]    # 100으로 나누고 시작
    visited = [0] * (n+1)
    max_per = 0
    per(0, 1)
    print(f'#{tc} {max_per*100:.6f}') # 확률이니깐 마지막 답에 100을 곱해준다.



