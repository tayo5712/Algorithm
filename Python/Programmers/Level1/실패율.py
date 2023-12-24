def solution(N, stages):
    answer = []
    challenger = [0] * (N+2)
    for stage in stages:
        challenger[stage] += 1
    
    total = len(stages)
    fail = {}
    for i in range(1, N+1):
        if challenger[i] == 0:
            fail[i] = 0
        else:
            fail[i] = challenger[i] / total
            total -= challenger[i]
    answer = sorted(fail, key = lambda x : fail[x], reverse=True)
    return answer
