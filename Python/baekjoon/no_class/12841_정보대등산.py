import sys
input = sys.stdin.readline

n = int(input()) # 지점의 개수(=횡단보도 수)
cross = list(map(int, input().split()))
left = [0] + list(map(int, input().split()))
right = [0] + list(map(int, input().split()))

left_sum, right_sum = [], []

temp = 0
temp2 = 0
for i in range(n):
    # 왼쪽 누적합
    temp += left[i]
    left_sum.append(temp)

    # 오른쪽 누적합
    temp2 += right[i]
    right_sum.append(temp2)

# 최소 거리
for i in range(n):
    if i == 0:
        min = left_sum[i] + right_sum[n-1]-right_sum[i]+ cross[i]
        min_cross = 0

    result = left_sum[i] + right_sum[n-1]-right_sum[i]+ cross[i]

    if result < min:
        min_cross = i
        min = result

print(min_cross+1, min)
