from collections import deque
maxL = int(input())
q = deque()

while True:
    n = int(input())
    if n == -1:
        if len(q) == 0:
            print("empty")
        else:
            for num in q:
                print(num, end = ' ')
        break

    elif n == 0:
        q.popleft()

    else:
        if len(q) < maxL:
            q.append(n)
