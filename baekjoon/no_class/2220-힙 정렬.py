import heapq

n = int(input())
heap = []
for num in range(2, n+1):       # 1이 가장 맨 뒤에 있으면 swap이 최대가 되기 때문에 1을 제외한 2부터 n 까지 최대 힙 정렬을 해준다.
    heapq.heappush(heap, (-num, num))

result = []
for i in heap:
    result.append(i[1])
result.append(1)            # 마지막에 1 추가

print(*result)
