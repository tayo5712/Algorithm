T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, n):
        if i == 1:  # 2번 째 칸은 자신의 왼쪽의 대각선 칸밖에 못 뗌
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]
        else:   # 3번 째 칸 부터는 자신의 왼쪽의 대각선 칸을 떼거나 그 왼쪽 것을 떼는 경우가 있으므로 둘 중 최대값을 더해줌
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

    print(max(sticker[0][n-1], sticker[1][n-1]))    # 마지막 인덱스 행 비교