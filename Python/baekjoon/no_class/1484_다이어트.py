ans = []
g = int(input())
left = 1
right = 2
while (left + right) <= 100000:
    now_g = right ** 2 - left ** 2
    if now_g < g:
        right += 1
    elif now_g > g:
        left += 1
    else:
        ans.append(right)
        right += 1

if len(ans) > 0:
    for ans_g in ans:
        print(ans_g)
else:
    print(-1)
