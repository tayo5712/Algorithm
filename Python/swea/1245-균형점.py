T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = arr[:n]
    mass = arr[n:]
    answer = [0] * (n-1)
    for i in range(n-1):   # 균형점은 n-1개
        left = pos[i]
        right = pos[i + 1]
        while right - left > 1 / (10**12):  # 좌표 값의 오차가 10 ** -12 보다 작으면 빠져나감
            mid = (left + right) / 2
            left_power = 0
            right_power = 0
            for j in range(n):
                if pos[j] < mid:    # 왼쪽 자성체
                    left_power += mass[j] / (mid-pos[j])**2
                else:   # 오른쪽 자성체
                    right_power += mass[j] / (pos[j]-mid)**2
            if left_power > right_power:
                left = mid
            else:
                right = mid
        answer[i] = mid
    print(f'#{tc}', end=" ")
    for balance in answer:
        print(f'{balance:.10f}', end=" ")
    print()