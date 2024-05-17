def solution(t, p):
    answer = 0
    n = len(p)
    l = 0
    while l + n <= len(t):
        if int(t[l:l + n]) <= int(p):
            answer += 1
        l += 1
    return answer
