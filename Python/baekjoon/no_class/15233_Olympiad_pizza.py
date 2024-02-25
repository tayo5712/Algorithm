from collections import deque

n = int(input())
answer = [0] * n
lst = list(map(int, input().split()))
q = deque()
for idx, num, in enumerate(lst):
    q.append((idx, num))
t = 1
while q:
    idx, need = q.popleft()
    if need == 1:
        answer[idx] = t
    else:
        q.append((idx, need - 1))
    t += 1
print(*answer)

