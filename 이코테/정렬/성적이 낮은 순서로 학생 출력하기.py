n = int(input())
lst = list(input().split() for _ in range(n))
chart = sorted(lst, key=lambda score: int(score[1]))
for i in chart:
    print(i[0], end = ' ')