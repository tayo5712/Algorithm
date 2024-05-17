def solution(s, skip, index):
    answer = ''
    for word in s:
        cnt = 1
        t = 1
        while t <= index:
            next = chr(((ord(word) + cnt) - 97) % 26 + 97)
            if next not in skip:
                t += 1
            cnt += 1
        answer += next
        print(next, cnt)

    return answer
