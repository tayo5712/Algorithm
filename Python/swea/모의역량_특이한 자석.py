T = int(input())
for tc in range(1, T+1):
    K = int(input())
    Magnetic = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        N, D = map(int, input().split())    # D가 1일 경우 시계, -1일 경우 반시계
        N -= 1      # 인덱스 맞춰주기
        move = [(N, D)]     # 톱니는 동시에 움직이니깐, 배열에 움직이는 경로를 담아두고 나중에 한번에 돌리기

        pole = D
        for i in range(N+1, 4):     # 오른쪽 자석들
            if Magnetic[i-1][2] != Magnetic[i][6]:      # 극이 다르면
                pole *= -1  # 극 바꿔주기
                move.append((i, pole))      # 움직이는 경로 담아두기
            else:
                break   # 극이 다르면 더 이상 보지 않아도 됨

        pole = D
        for i in range(N-1, -1, -1):    # 왼쪽 자석들
            if Magnetic[i][2] != Magnetic[i+1][6]:
                pole *= -1
                move.append((i, pole))
            else:
                break

        # 움직이기
        for i, d in move:
            if d == 1:  # 시계 방향 회전일 경우
                tmp = Magnetic[i].pop()
                Magnetic[i].insert(0, tmp)
            else:
                tmp = Magnetic[i].pop(0)
                Magnetic[i].append(tmp)

    # 점수 계산
    result = 0
    for i in range(4):
        result += Magnetic[i][0] * (2**i)

    print(f"#{tc} {result}")


