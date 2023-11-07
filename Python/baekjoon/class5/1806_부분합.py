n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = 100001
sum = 0
length = 0
lt = 0
for rt in range(n):
    sum += arr[rt]
    length += 1
    if sum >= s:
        result = min(result, length)
    while sum > s:
        sum -= arr[lt]
        lt += 1
        length -= 1
        if sum >= s:
            result = min(result, length)

if result == 100001:
    print(0)
else:
    print(result)