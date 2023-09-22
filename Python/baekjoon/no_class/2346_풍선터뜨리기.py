n = int(input())
papers = list(enumerate(map(int, input().split())))  # 풍선 안의 종이에 적혀 있는 수
p = 1
move = 0
while n:
    p += move
    if move < 0:
        p %= n
    else:
        p = (p - 1) % n
    idx, move = papers.pop(p)
    n -= 1
    print(idx + 1, end=' ')