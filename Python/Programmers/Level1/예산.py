def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        if money <= budget:
            answer += 1
            budget -= money
        else:
            break
    return answer
