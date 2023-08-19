dx = [0, 0, 1, 0, -1]  # 상우하좌
dy = [0, -1, 0, 1, 0]

def Check(a_charge, b_charge):
    global answer, a_man, b_man
    maxV1, used = 0, -1
    for charge in a_charge:     # a가 먼저 선택
        maxV1 += charge[0]
        used = charge[1]        # 사용한 충전기 인덱스 저장
        break
    for charge in b_charge:     # b의 사용 가능 충전기 중 a가 사용 안한거 있으면 사용
        if charge[1] != used:   # 어차피 둘이 같이 사용할 경우 한 충전기의 충전량으로 같음
            maxV1 += charge[0]
            break

    maxV2, used = 0, -1
    for charge in b_charge:     # 위의 예시 반대로
        maxV2 += charge[0]
        used = charge[1]
        break
    for charge in a_charge:
        if charge[1] != used:
            maxV2 += charge[0]
            break
    answer += max(maxV1, maxV2)

def Move():
    for d in range(M+1):    # 초기 위치부터 확인하기 위해 범위 1 늘려줌
        a_charge, b_charge = [], []
        for i in range(A):
            bx, by, area, charge = BC[i][0], BC[i][1], BC[i][2], BC[i][3]
            if abs(bx-a_man[0]) + abs(by-a_man[1]) <= area:     # 범위 확인
                a_charge.append([charge, i])
            if abs(bx-b_man[0]) + abs(by-b_man[1]) <= area:
                b_charge.append([charge, i])
        a_charge.sort(reverse=True)     # 처리량순으로 내림차순
        b_charge.sort(reverse=True)
        Check(a_charge, b_charge)

        if d == M:  # 마지막으로 움직이고 난 뒤에 종료
            break
        a_man[0] += dx[a_move[d]]   # 다음 칸 이동
        a_man[1] += dy[a_move[d]]
        b_man[0] += dx[b_move[d]]
        b_man[1] += dy[b_move[d]]

T = int(input())
for tc in range(1, T + 1):
    answer = 0
    a_man = [1, 1]
    b_man = [10, 10]
    M, A = map(int, input().split())
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(A)]
    Move()
    print(f'#{tc} {answer}')
