from collections import deque

def bfs(x):

    q = deque()
    q.append([x])

    while q:
        target = q.popleft()
        x = target[-1]
        if x == 1:  # 연산된 값이 1이면 그 리스트를 반환
            return target

        if x % 3 == 0:  # 연산된 값이 3으로 나누어 떨어지면, 기존 리스트에 연산된 값(3으로 나눈값)을 추가한 뒤 큐에 추가
            q.append(target + [x // 3])

        if x % 2 == 0: # 연산된 값이 2로 나누어 떨어지면, 기존 리스트에 연산된 값(2로 나눈값)을 추가한 뒤 큐에 추가
            q.append(target + [x // 2])

        q.append(target + [x - 1])  # 마지막 연산된 값에서 1을 빼고 기존 리스트에 추가한 뒤 큐에 추가

n = int(input())
result = bfs(n)
print(len(result) - 1)
print(*result)