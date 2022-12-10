def divide(stx, sty, n):
    global white, blue
    start = paper[stx][sty]
    for i in range(stx, stx + n):
        for j in range(sty, sty + n):
            if start != paper[i][j]:
                for a in range(2):
                    for b in range(2):
                        divide(stx + a * (n//2), sty + b * (n//2), n//2)
                return

    if start == 0:
        white += 1
    else:
        blue += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
divide(0, 0, n)

print(white)
print(blue)