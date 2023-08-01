from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
cnt = 1
answer = []
while q:
    target = q.popleft()
    if cnt == k:
        answer.append(target)
        cnt = 1
    else:
        q.append(target)
        cnt += 1

answer = str(answer).replace("[", "<").replace("]", ">")
print(answer)
# print("<", end="")
# for i in range(n-1):
#     print(f"{answer[i]}, ", end="")
# print(f"{answer[-1]}>")
