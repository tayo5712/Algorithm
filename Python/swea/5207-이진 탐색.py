import sys
sys.stdin = open("input_5207.txt", "r")

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        check = None    # 왼쪽으로 갔는지 오른쪽으로 갔는지 확인용
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2

            if A[mid] == b:     # mid 값이 찾는 값이면 cnt + 1
                cnt += 1
                break

            elif A[mid] < b:    # mid 값이 찾는 값 보다 작으면
                if check == True:   # 만약 그 전의 찾는 방향이 오른쪽이면 break
                    break
                left = mid + 1      # left를 mid+1로 바꾸줌 (오른쪽 탐색)
                check = True        # 오른쪽 탐색을 함으로 표시 바꿔주기

            elif A[mid] > b:
                if check == False:
                    break
                right = mid - 1
                check = False

    print(f'#{tc} {cnt}')


