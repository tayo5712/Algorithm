from collections import deque

n, l, w = map(int, input().split())
trucks = list(map(int, input().split()))

q = deque()
q.append([trucks[0], 1])
cnt = 1
index = 1
weight = trucks[0]

while q:
    cnt += 1
    for i in range(len(q)):
        q[i][1] += 1
    if q[0][1] > l:
        weight -= q.popleft()[0]
    if index < len(trucks):
        if w >= weight + trucks[index]:
            q.append([trucks[index], 1])
            weight += trucks[index]
            index += 1

print(cnt)
