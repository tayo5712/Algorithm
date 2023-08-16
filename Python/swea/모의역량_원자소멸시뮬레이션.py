dx = [0, 0, -0.5, 0.5]  # 상하좌우 (좌표 중간에서 만나는 경우도 고려 (0.5단위))
dy = [0.5, -0.5, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    atoms = [list(map(int, input().split())) for _ in range(N)]
    while len(atoms) > 1:    # 원자가 두개 이상일 때만
        collision = {}
        for atom in atoms:
            x, y, d, energy = atom
            nx, ny = x + dx[d], y + dy[d]
            if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:     # 해당 범위 밖으로 나가면 어차피 만날 수 없음
                if (nx, ny) not in collision:
                    collision[(nx, ny)] = []
                collision[(nx, ny)].append([nx, ny, d, energy])
        atoms = []  # 원자 배열 초기화
        for key, value in collision.items():
            if len(value) == 1:     # 해당 좌표에 원자가 한 개이면 충돌한 개 아니므로 다시 원자 배열에 넣어줌
                atoms.append(value[0])
            else:       # 해당 좌표에 원자가 여러개 이면 충돌한 것 이므로 에너지를 합해줌
                for atom in value:
                    answer += atom[3]

    print(f'#{tc} {answer}')