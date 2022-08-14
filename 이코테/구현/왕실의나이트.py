T = input()

row = int(T[1])
col = int(ord(T[0])-ord('a')+1)

step = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
cnt = 0

for i, j in step:
    nr = row + i
    nc = col + j
    if nr < 1 or nr > 8 or nc < 1 or nc > 8:
        continue
    cnt += 1

print(cnt)