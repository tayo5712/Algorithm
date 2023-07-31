from collections import deque

ss = list(input())
q = deque(ss)
tmp = []
answer = ""
while q:
    c = q.popleft()
    if c == "<":
        while tmp:
            answer += tmp.pop()
        answer += c
        while True:
            cc = q.popleft()
            answer += cc
            if cc == ">":
                break
    elif c == " ":
        while tmp:
            answer += tmp.pop()
        answer += c
    else:
        tmp.append(c)
while tmp:
    answer += tmp.pop()
print(answer)
