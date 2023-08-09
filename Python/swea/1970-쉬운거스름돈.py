T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    answer = [0] * 8
    n = int(input())
    for i in range(8):
        answer[i] = n // money[i]
        n %= money[i]
    print(f'#{tc}')
    print(*answer)