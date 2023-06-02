import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mapp = [list(input()) for _ in range(n)]
sti, stj = 0, 0
std = ""
flag = True
for i in range(n):
    for j in range(m):
        if mapp[i][j] == "#":
            isStart = 0
            if j + 1 < m and mapp[i][j+1] == "#":
                isStart += 1
                std = ">"
            if j - 1 >= 0 and mapp[i][j-1] == "#":
                isStart += 1
                std = "<"
            if i + 1 < n and mapp[i+1][j] == "#":
                isStart += 1
                std = "v"
            if i - 1 >= 0 and mapp[i-1][j] == "#":
                isStart += 1
                std = "^"
            if isStart == 1:
                sti = i
                stj = j
                flag = False
                break
    if not flag:
        break

result = ""
curd = std
curi = sti
curj = stj
while True:
    if curd == ">":
        if curj+1 < m and curj+2 < m and mapp[curi][curj+1] == "#" and mapp[curi][curj+2] == "#":
            mapp[curi][curj+1] = "."
            mapp[curi][curj+2] = "."
            result += "A"
            curj = curj + 2
        elif curi-1 >= 0 and curi-2 >= 0 and mapp[curi-1][curj] == "#" and mapp[curi-2][curj] == "#":
            mapp[curi - 1][curj] = "."
            mapp[curi - 2][curj] = "."
            result += "LA"
            curd = "^"
            curi = curi-2
        elif curi+1 < n and curi+2 < n and mapp[curi+1][curj] == "#" and mapp[curi+2][curj] == "#":
            mapp[curi+1][curj] = "."
            mapp[curi+2][curj] = "."
            result += "RA"
            curd = "v"
            curi = curi+2
        else:
            break
    elif curd == "<":
        if curj-1 >= 0 and curj-2 >= 0 and mapp[curi][curj-1] == "#" and mapp[curi][curj-2] == "#":
            mapp[curi][curj-1] = "."
            mapp[curi][curj-2] = "."
            result += "A"
            curj = curj - 2
        elif curi+1 < n and curi+2 < n and mapp[curi+1][curj] == "#" and mapp[curi+2][curj] == "#":
            mapp[curi+1][curj] = "."
            mapp[curi+2][curj] = "."
            result += "LA"
            curd = "v"
            curi = curi+2
        elif curi-1 >= 0 and curi-2 >= 0 and mapp[curi-1][curj] == "#" and mapp[curi-2][curj] == "#":
            mapp[curi-1][curj] = "."
            mapp[curi-2][curj] = "."
            result += "RA"
            curd = "^"
            curi = curi-2
        else:
            break
    elif curd == "^":
        if curi-1 >= 0 and curi-2 >= 0 and mapp[curi-1][curj] == "#" and mapp[curi-2][curj] == "#":
            mapp[curi-1][curj] = "."
            mapp[curi-2][curj] = "."
            result += "A"
            curi = curi - 2
        elif curj-1 >= 0 and curj-2 >= 0 and mapp[curi][curj-1] == "#" and mapp[curi][curj-2] == "#":
            mapp[curi][curj-1] = "."
            mapp[curi][curj-2] = "."
            result += "LA"
            curd = "<"
            curj = curj-2
        elif curj+1 < m and curj+2 < m and mapp[curi][curj+1] == "#" and mapp[curi][curj+2] == "#":
            mapp[curi][curj+1] = "."
            mapp[curi][curj+2] = "."
            result += "RA"
            curd = ">"
            curj = curj+2
        else:
            break
    else:
        if curi+1 < n and curi+2 < n and mapp[curi+1][curj] == "#" and mapp[curi+2][curj] == "#":
            mapp[curi+1][curj] = "."
            mapp[curi+2][curj] = "."
            result += "A"
            curi = curi + 2
        elif curj+1 < m and curj+2 < m and mapp[curi][curj+1] == "#" and mapp[curi][curj+2] == "#":
            mapp[curi][curj+1] = "."
            mapp[curi][curj+2] = "."
            result += "LA"
            curd = ">"
            curj = curj+2
        elif curj-1 >= 0 and curj-2 >= 0 and mapp[curi][curj-1] == "#" and mapp[curi][curj-2] == "#":
            mapp[curi][curj-1] = "."
            mapp[curi][curj-2] = "."
            result += "RA"
            curd = "<"
            curj = curj-2
        else:
            break
print(sti+1, stj+1)
print(std)
print(result)