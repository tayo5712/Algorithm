T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 1e10

    stairs = []
    people = []
    num_p = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] > 1:
                stairs.append([r, c, board[r][c]])
            if board[r][c] == 1:
                num_p += 1
                people.append([r, c])

    for i in range(1 << num_p):
        which_stair = [0] * num_p
        for j in range(num_p):
            if i & (1 << j):
                which_stair[j] = 1
        dist_p_s = [0] * num_p
        for idx in range(num_p):
            stair_r, stair_c, _ = stairs[which_stair[idx]]
            person_r, person_c = people[idx]
            dist = abs(stair_r-person_r) + abs(stair_c-person_c)
            dist_p_s[idx] = dist

        stairs_info = [[-1, -1, -1], [-1, -1, -1]]
        stairs_waiting = [0, 0]

        taken_time = 0
        while True:
            if taken_time >= answer:
                break
            terminate_flag = True
            for idx in range(num_p):
                if dist_p_s[idx] >= -1:
                    terminate_flag = False

            for stair in range(2):
                if stairs_waiting[stair] > 0:
                    terminate_flag = False

            for stair in range(2):
                for position in range(3):
                    if stairs_info[stair][position] > 0:
                        terminate_flag = False

            if terminate_flag:
                break

            for stair in range(2):
                for position in range(3):
                    if stairs_info[stair][position] == 0:
                        stairs_info[stair][position] -= 1

            for idx in range(num_p):
                if dist_p_s[idx] == -1:
                    stair_idx = which_stair[idx]
                    stairs_waiting[stair_idx] += 1

            for stair in range(2):
                flag = True
                while stairs_waiting[stair] and flag:
                    for idx in range(3):
                        if stairs_info[stair][idx] == -1:
                            stairs_info[stair][idx] = stairs[stair][2]
                            stairs_waiting[stair] -= 1
                            break
                    else:
                        flag = False

            for idx in range(num_p):
                if dist_p_s[idx] >= -1:
                    dist_p_s[idx] -= 1
            for stair in range(2):
                for position in range(3):
                    if stairs_info[stair][position] > 0:
                        stairs_info[stair][position] -= 1

            taken_time += 1

        if taken_time < answer:
            answer = taken_time

    print(f'#{tc} {answer}')