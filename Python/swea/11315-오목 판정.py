import sys
sys.stdin = open("input_11315.txt", "r")

def omok():
    for i in range(n):
        for j in range(n):
            for di, dj in [[0, 1], [1, 0], [1, 1], [-1, 1]]:        # 오른쪽, 아래, 오른쪽 아래 대각선, 오른쪽 위 대각선
                for k in range(5):      # 오목 이니깐 5번 연속으로 돌이 있는지만 확인
                    ni = i + di * k
                    nj = j + dj * k
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 'o':    # 범위 밖이 아니고 돌이 있을 때
                        pass    # 다음 칸 확인
                    else:       # 연속적으로 돌이 이어지지 않으면 break
                        break
                else:           # for문 5번 돌면 오목이 된거니깐 yes 리턴
                    return 'YES'
    return 'NO' # 모든 칸을 전부 다 돌았는데 조건에 만족하는게 없으면 no 리턴

for tc in range(1, int(input())+1):
    n = int(input())
    board = [input() for _ in range(n)]

    print(f'#{tc} {omok()}')

