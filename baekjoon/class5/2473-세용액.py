n = int(input())
arr = list(map(int, input().split()))
arr.sort()

minV = 3000000000
a, b, c = 0, 0, 0
for i in range(n-2):    # 기준점 생성. #후엔 2467용액 문제와 똑같음
    left = i + 1
    right = n-1
    while left < right:
        value = arr[i] + arr[left] + arr[right]
        value_a = abs(arr[i] + arr[left] + arr[right])
        if value_a < minV:
            minV = value_a
            a, b, c = arr[i], arr[left], arr[right]
        if value > 0:
            right -= 1
        elif value < 0:
            left += 1
        else:
            break

print(a, b, c)