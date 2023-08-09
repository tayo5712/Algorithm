T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customers = sorted(list(map(int, input().split())))
    answer = "Possible"
    for i in range(N):
        if customers[i] // M * K - i <= 0:
            answer = "Impossible"
            break
    print(f'#{tc} {answer}')