
import sys

sys.stdin = open("input_2382.txt", "r")

# (상: 1, 하: 2, 좌: 3, 우: 4)

for tc in range(1, int(input())+1):
    n, m, k = map(int,input().split())
    zone = [[0 for _ in range(n)] for _ in range(n)]

    cell_info = [list(map(int, input().split())) for _ in range(k)]
    for time in range(m):   # 시간
        cell_info.sort(key=lambda x:x[2])   # 미생물 수를 기준으로 정렬
        for cell in cell_info:
            if not cell[2]:                 # 미생물 수가 0일경우 continue
                continue
            '''
            cell[0] = 세로
            cell[1] = 가로
            cell[2] = 세포수
            cell[3] = 이동방향
            '''
            if cell[3] == 1:                # 미생물의 이동방향이 위쪽이면
                cell[0] -= 1                # r 좌표 - 1
                if cell[0] == 0 or cell[0] == (n-1):    # 미생물의 좌표가 약품 위이면
                    cell[2] //= 2                       # 미생물의 수를 //2 하고
                    cell[3] = 2                         # 미생물의 방향을 바꾼다.

            elif cell[3] == 2:
                cell[0] += 1
                if cell[0] == 0 or cell[0] == (n-1):
                    cell[2] //= 2
                    cell[3] = 1

            elif cell[3] == 3:
                cell[1] -= 1
                if cell[1] == 0 or cell[1] == (n-1):
                    cell[2] //= 2
                    cell[3] = 4

            elif cell[3] == 4:
                cell[1] += 1
                if cell[1] == 0 or cell[1] == (n-1):
                    cell[2] //= 2
                    cell[3] = 3

        # 미생물 군집이 같은 칸에 있는지 확인
        # 현재 미생물 군집의 리스트는 미생물 의 수를 기준으로 오름차순 정렬되어 있다.

        for i in range(k-1):
            for j in range(i+1, k):
                if cell_info[i][0] == cell_info[j][0] and cell_info[i][1] == cell_info[j][1]:   # 좌표값이 같으면

                    cell_info[j][2] += cell_info[i][2]      # 미생물 수가 더 많은 군집에 미생물 수가 적은 군집의 미생 물수를 더해준다.

                    cell_info[i][2] = 0                     # 미생물 수가 더 적은 군집의 미생물 수를 0으로 만들고
                    cell_info[i][0] = -1                    # 그 좌표를 못쓰게 하기 위해서 -1 처리를 한다.
                    cell_info[i][1] = -1

                    break                                   # 미생물이 적은 군집은 소멸 했기 때문에 더이상 확인 불가

    sumV = 0
    for cell in cell_info:         # 각 칸의 남은 미생물 수 확인
        sumV += cell[2]

    print(f'#{tc} {sumV}')

