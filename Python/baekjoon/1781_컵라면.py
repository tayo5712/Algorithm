from heapq import heappop, heappush

n = int(input())
result = 0
heap = []
arr = sorted(list(list(map(int, input().split()))) for _ in range(n))

for t, c_r in arr:
    heappush(heap, c_r)
    if t < len(heap):
        heappop(heap)

print(sum(heap))


