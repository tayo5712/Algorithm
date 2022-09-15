import sys
input = sys.stdin.readline
n = int(input())
room =[list(map(int, input().split())) for _ in range(n)]
room.sort(key=lambda x: x[0])       # 시작과 동시에 끝나는 경우가 있으므로 시작시간으로 먼저 정렬
room.sort(key=lambda x: x[1])       # 종료시간이 빠른 순서대로 정렬

pre = room[0][1]
cnt = 1

for i in range(1, n):               # 전의 회의의 종료시간이 현재 회의의 시작시간보다 작거나 같으면
    if pre <= room[i][0]:
        cnt += 1
        pre = room[i][1]

print(cnt)


# 시간 초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = sorted(list(map(int, input().split())) for _ in range(n))
# print(arr)

# maxV = 0
# for i in range(0, len(arr)-1):
#     cnt = 1
#     a = i
#     for j in range(i+1, len(arr)):
#         if arr[a][1] <= arr[j][0]:
#             cnt += 1
#             a = j
#     maxV = max(maxV, cnt)
# print(maxV)