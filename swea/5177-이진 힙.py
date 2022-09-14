import sys

sys.stdin = open("input_5177 (2).txt", "r")

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())       # 목표 노드
#     node = [0] + list(map(int, input().split()))
#     for i in range(2, n+1):
#         while node[i//2] > node[i]:     # 부모 노드가 자식 노드 보다 크면 위치 바꾸기
#             node[i//2], node[i] = node[i], node[i//2]
#             i //= 2         # 다음 부모 노드 확인
#
#     answer = 0
#     while n > 1:
#         n //= 2
#         answer += node[n]
#     print(f'#{tc} {answer}')

# heapq 모듈 사용

import heapq
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    heap = [0] + heap
    answer = 0
    while n > 1:
        n //= 2
        answer += heap[n]
    print(f'#{tc} {answer}')