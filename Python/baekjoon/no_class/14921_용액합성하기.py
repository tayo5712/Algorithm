n = int(input())
arr = list(map(int, input().split()))
answer = float('inf')
lt = 0
rt = n - 1
while lt < rt:
    sumV = arr[lt] + arr[rt]
    if abs(sumV) < abs(answer):
        answer = sumV
    if sumV < 0:
        lt += 1
    elif sumV > 0:
        rt -= 1
    else:
        break
print(answer)
