"""
4
홍길동 95
이순신 77
대조영 88
정약용 99
"""

n = int(input())
array = [input().split() for _ in range(n)]
order = sorted(array, key=lambda score: int(score[1]))
for i in order:
    print(i[0], end=" ")

# n = int(input())
# lst = list(input().split() for _ in range(n))
# chart = sorted(lst, key=lambda score: int(score[1]))
# for i in chart:
#     print(i[0], end = ' ')