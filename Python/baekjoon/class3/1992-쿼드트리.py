def divide(sti, stj, n):
    start = arr[sti][stj]   # 시작점 값
    for i in range(sti, sti + n):
        for j in range(stj, stj + n):
            if start != arr[i][j]:
                print('(', end='')  # 범위 안에 숫자가 같지 않으면 압축 준비 '(' 프린트
                for x in range(2):      # 4개로 영역을 나눠서 재탬색
                    for y in range(2):
                        divide(sti + x * (n//2), stj + y * (n//2), n//2)
                print(')', end='')  # 4 구역 확인 후 압축 ')' 프린트
                return

    if start == 1:
        print(1, end='')
    else:
        print(0, end='')


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
divide(0, 0, n)