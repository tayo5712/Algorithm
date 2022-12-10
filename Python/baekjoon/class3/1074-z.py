n, r, c = map(int, input().split())

cnt = 0
while n != 0:
    section = 2 ** (n-1)    # 사분면 나누는 기준
    if r < section and c < section:     # 1사분면
        cnt += 0        # 지나쳐 온 만큼 개수 추가

    elif r < section and c >= section:  # 2사분면
        cnt += section * section    # 지나쳐 온 만큼 개수 추가
        c -= section                # 다음 범위에 맞게 R, C값 재설정

    elif r >= section and c < section:  # 3사분면
        cnt += (section * section) * 2
        r -= section

    elif r >= section and c >= section: # 4사분면
        cnt += (section * section) * 3
        r -= section
        c -= section

    n -= 1      # 사분면을 나누고 해당 범위에 가서 또 사분면을 나눔

print(cnt)


# 초고수가 푼 비트연산 방법
# n,r,c=map(int,input().split());print(int(f'{c:b}',4)+2*int(f'{r:b}',4))

# 메모리 초과 (브루트포스)
# n, r, c = map(int, input().split())
# arr = [[0] * 2 ** n for _ in range(2 ** n)]
#
# def z_arr(arr):
#     num = 0
#     for i in range(0, 2 ** n, 2 ** (n-1)):
#         for j in range(0, 2 ** n, 2 ** (n-1)):
#             for a in range(i, i + (2 ** (n-1)), 2):
#                 for b in range(j, j + (2 ** (n-1)), 2):
#                     for di, dj in [[0, 0], [0, 1], [1, 0], [1, 1]]:
#                         arr[a+di][b+dj] = num
#                         if a+di == r and b+dj == c:
#                             return num
#                         num += 1
#
# print(z_arr(arr))
