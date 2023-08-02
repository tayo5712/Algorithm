T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    # 회전 수는 자릿수 - 1
    lock = input()
    jari = n // 4
    answer = set()
    for _ in range(jari):
        for i in range(0, n, jari):
            answer.add(lock[i:i+jari])
        lock = lock[1:] + lock[0]
    answer = list(answer)
    answer = sorted(answer, key=lambda x: -int(x, 16))
    print(f'#{tc} {int(answer[k-1], 16)}')