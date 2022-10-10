from heapq import heappush, heappop

for _ in range(int(input())):
    n = int(input())
    minH, maxH = [], []     # 최소힙, 최대힙
    visited = [0] * n   # 지운 숫자 인지 확인용
    for i in range(n):
        order, num = input().split()
        num = int(num)

        if order == 'I':
            heappush(minH, (num, i))
            heappush(maxH, (-num, i))
            visited[i] = 1      # 숫자 사용하기

        else:
            if num == -1:
                while minH and not visited[minH[0][1]]:     # 최소힙의 맨 앞이 최대힙에서 지운 숫자이면 최소힙에서도 지움
                    heappop(minH)
                if minH:
                    visited[minH[0][1]] = 0     # 숫자 지운표시 하기
                    heappop(minH)
            else:
                while maxH and not visited[maxH[0][1]]:
                    heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = 0
                    heappop(maxH)

    while minH and not visited[minH[0][1]]:     # 다 돌고나서 남은 사용한 숫자 제거
        heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heappop(maxH)

    if minH and maxH:
        print(-maxH[0][0], minH[0][0])
    else:
        print("EMPTY")