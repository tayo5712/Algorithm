from heapq import heappush, heappop, heapify

N = int(input())
cards = list(int(input()) for _ in range(N))
heapify(cards)
answer = 0
while len(cards) > 1:
        a, b = heappop(cards), heappop(cards)
        answer += a + b
        heappush(cards, a + b)
print(answer)
