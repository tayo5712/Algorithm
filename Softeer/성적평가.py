from heapq import heappush, heappop

def com(round, flag):
    global total
    heap = []
    for i in range(n):
        if flag:
            total[i] += round[i]
        heappush(heap, (-round[i], i))
    result = [0] * n
    same = 0
    rank = 0
    before_score = -3003
    while heap:
        score, index = heappop(heap)
        if score > before_score:
            rank += same + 1
            same = 0
            result[index] = rank
            before_score = score
        else:
            result[index] = rank
            same += 1
    print(*result)

n = int(input())
round1 = list(map(int, input().split()))
round2 = list(map(int, input().split()))
round3 = list(map(int, input().split()))
total = [0] * n

com(round1, True)
com(round2, True)
com(round3, True)
com(total, False)
