def solution(n, m, section):
    answer = 1
    now = section[0] + (m - 1)
    for s in section:
        if s <= now:
            continue
        else:
            now = s + (m - 1)
            answer += 1
    
    return answer
