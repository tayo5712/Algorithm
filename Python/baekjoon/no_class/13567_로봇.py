M, n = map(int, input().split())

dr = [1, 0, -1, 0] # 남, 서, 북, 동
dc = [0, -1, 0, 1]
pos = 0
now_r, now_c = 0, 0

for _ in range(n):
    order, d = input().split()
    d = int(d)
    if order == 'MOVE':
        next_r = now_r + dr[pos] * d
        next_c = now_c + dc[pos] * d
        if 0 <= next_r <= M and 0 <= next_c <= M:
            now_r = next_r
            now_c = next_c
        else:
            print(-1)
            break
    elif order == 'TURN':
        if d == 0: # 왼쪽 회전
            pos = (pos + 3) % 4
        else: # 오른쪽 회전
            pos = (pos + 1) % 4
else:
    print(now_r, now_c)
