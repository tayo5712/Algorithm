n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))

left = min(arr)
right = m * max(arr)
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0
    for num in arr:
        total += mid // num

    if total >= m:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)
