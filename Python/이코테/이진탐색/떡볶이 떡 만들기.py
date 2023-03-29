"""
4 6
19 15 10 17
"""
# 이진탐색
# def binary(target, rices, st, ed):
#     global result
#     if st > ed:
#         return
#     mid = (st + ed) // 2
#     total = 0 # 잘린 떡의 양
#     for rice in rices:
#         if mid < rice: # 떡 길이가 잘리는 길이보다 길 때만 잘린 떡의 양에 합산
#             total += (rice-mid)
#     if total >= target: # 잘린 떡의 양이 원하는 떡길이 양과 같거나 클 경우
#         result = max(mid, result) # 잘리는 최대 길이를 구해줌
#         binary(target, rices, st+1, ed) # 다시 이진 탐색
#     else:
#         binary(target, rices, st, ed-1)
#
# result = 0;
# n, m = map(int, input().split())
# rice = list(map(int, input().split()))
# binary(m, rice, 0, max(rice))
# print(result)

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)