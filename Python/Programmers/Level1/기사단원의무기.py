def yaksu(n):
    tmp = 0
    for i in range(1, int(n ** 0.5) + 1):
        if i * i == n:
            tmp += 1
        elif n % i == 0:
            tmp += 2
    return tmp
        
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        p = yaksu(i)
        answer += p if p <= limit else power
    return answer
