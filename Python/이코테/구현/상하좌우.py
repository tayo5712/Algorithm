N = int(input())
move = input().split()
x, y = 1, 1
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
d = ['L', 'R', 'U', 'D']

for i in move:
    for j in range(len(d)):
        if i == d[j]:
            nx = x + dr[j]
            ny = y + dc[j]
            if nx < 1 or nx > N or ny < 1 or ny > N:
                continue
            x = nx
            y = ny

print(x, y)