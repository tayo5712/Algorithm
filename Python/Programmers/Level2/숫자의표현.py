def solution(n):
    answer = 0
    sumV = 0
    k = 1
    for i in range(1, n + 1):
        sumV += i
        while sumV > n:
            sumV -= k
            k += 1
        if sumV == n:
            answer += 1
                     
    return answer
