# 구간 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr =[0]
sumV = 0
for i in arr:
    sumV += i
    sum_arr.append(sumV)

for _ in range(m):
    st, ed = map(int, input().split())
    print(sum_arr[ed]-sum_arr[st-1])


# 시간초과
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# for _ in range(m):
#     st, ed = map(int, input().split())
#     print(sum(arr[st-1:ed]))