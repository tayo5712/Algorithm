from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    word = list(map(str, input().split()))
    if word[0] == "push":
        q.append(word[1])
    else:
        if word[0] == "pop":
            print(q.popleft() if len(q) != 0 else -1)
        elif word[0] == "size":
            print(len(q))
        elif word[0] == "empty":
            print(1 if len(q) == 0 else 0)
        elif word[0] == "front":
            print(q[0] if len(q) != 0 else -1)
        elif word[0] == "back":
            print(q[-1] if len(q) != 0 else -1)
