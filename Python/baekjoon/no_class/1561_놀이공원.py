n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = sum(arr) * (n // m + 1)
result = 0 # n명까지 모두 타는데 걸리는 시간 (마지막 아이가 놀이기구에 탑승하는 시점!!!!)

def possible(mid):
    cnt = 0
    for i in range(m):
        cnt += mid // arr[i] + 1
    if cnt >= n:
        return True
    else:
        return False

while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        right = mid - 1
        result = mid
    else:
        left = mid + 1

maxP = 0
for i in range(m):
    maxP += (result - 1) // arr[i] + 1

for i in range(m):
    if not result % arr[i]:
        maxP += 1
        if maxP == n:
            print(i + 1)
            break
