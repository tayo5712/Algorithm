import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]
result = 100000000                  # 시간 최소값 비교용
height = 0                          # 높이 변수
for idx in range(257):              # 높이는 0~256까지
    out_block, in_block = 0, 0      # 뺀 블록, 넣은 블록 변수
    for i in range(n):
        for j in range(m):
            if world[i][j] > idx:   # idx높이를 기준으로 더 크면
                out_block += world[i][j] - idx  # 큰 만큼 블럭을 빼주고
            else:
                in_block += idx - world[i][j]   # 작으면 작은 만큼 블럭을 넣어준다.
    if b + out_block >= in_block:               # 넣은 블럭이 뺀 블럭과 원래 인벤토리에 있던 b값보다 작거나 같아야 진행가능
        time = out_block * 2 + in_block         # 블럭을 뺼 땐 2초, 넣을 땐 1초로 걸린 시간 계산
        if time <= result:                      # 땅 고르기에 필요한 최소시간 (같거나 작을때를 써서 같은 시간일 경우 오름차순으로 진행하므로 높이가 더 높을 경우 출력)
            result = time
            height = idx

print(result, height)

# 시간초과
# for idx in range(257):
#     time = 0
#     inven = b
#     for i in range(n):
#         for j in range(m):
#             if world[i][j] > idx:
#                 time += ((world[i][j] - idx) * 2)
#                 inven += (world[i][j] - idx)
#             else:
#                 time += (idx - world[i][j])
#                 inven -= idx - world[i][j]
#
#     if inven < 0:
#         continue
#     if time <= result:
#         result = time
#         height = idx
#
# print(result, height)

