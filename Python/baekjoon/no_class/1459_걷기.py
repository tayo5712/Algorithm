x, y, w, s = map(int, input().split())
answer = 0
if 2*w <= s:
    print((x+y) * w)
else:
    answer = min(x, y) * s
    differ = abs(x-y)
    if w > s:
        if differ % 2:
            answer += (differ-1) * s + w
        else:
            answer += differ * s
    else:
        answer += differ * w
    print(answer)
