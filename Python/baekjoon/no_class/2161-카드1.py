from collections import deque

n = int(input())
deq = deque()
for i in range(1, n+1):
    deq.append(i)
result = []
while len(deq) > 1:
    result.append(deq.popleft())
    deq.append(deq.popleft())
print(*result, deq[0])


