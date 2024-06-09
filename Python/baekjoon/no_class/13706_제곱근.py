# 제곱근 이분탐색????

n = int(input())
l = 1
h = n

while True:
    mid = (l + h) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        h = mid - 1
    else:
        l = mid + 1
