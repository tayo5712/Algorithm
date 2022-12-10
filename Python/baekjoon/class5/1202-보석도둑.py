from heapq import heappop, heappush

n, k = map(int, input().split())
heap = []
for _ in range(n):  # (무게, 가치)로 heappush
    heappush(heap, list(map(int, input().split())))

c = [int(input()) for _ in range(k)]    # 가방 무게순으로 오름차순 정렬
c.sort()

result = 0
compare = []    # 가능한 보석 heap
for bag in c:
    while heap and bag >= heap[0][0]:   # 가방의 무게가 보석의 무게보다 클 경우
        heappush(compare, -heappop(heap)[1])    # compare에 가능한 모든 보석을 최대힙(-붙여서)으로 집어넣는다.

    if compare:     # compare가 있으면 그중 가장 최대의 가치를 가진 보석을 현재 가방에 넣는다.
        result -= heappop(compare)      # 최대힙은 넣을 때 -를 붙여서 넣기 때문에 -로 다시 더해준다.

print(result)