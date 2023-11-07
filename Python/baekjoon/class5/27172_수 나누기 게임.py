n = int(input())
players = list(map(int, input().split()))
cards = [False for _ in range(1000001)]
scores = [0 for _ in range(1000001)]

for i in range(n):
    cards[players[i]] = True

for i in players:
    for j in range(i*2, 1000001, i):
        if cards[j]:
            scores[i] += 1
            scores[j] -= 1

for i in players:
    print(scores[i], end=' ')

