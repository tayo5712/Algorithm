n = int(input())
lst = sorted(list(map(int, input().split())))
answer = 0
for i in range(1, n - 1):
    left = 0
    right = n - 1
    while left < i and right > i:
        sumV = lst[left] + lst[i] + lst[right]
        if sumV == 0:
            l_count = 1
            r_count = 1
            while left + 1 < i and lst[left] == lst[left+1]:
                left += 1
                l_count += 1
            while right - 1 > i and lst[right] == lst[right-1]:
                right -= 1
                r_count += 1
            answer += l_count * r_count
            left += 1
            right -= 1
        elif sumV < 0:
            left += 1
        else:
            right -= 1
print(answer)
