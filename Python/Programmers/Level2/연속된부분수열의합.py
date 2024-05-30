answer = [0, 999999]

def check(lt, rt):
    global answer
    if answer[1] - answer[0] > rt - lt:
        answer[0], answer[1] = lt, rt
    
def solution(sequence, k):
    lt = 0
    sumV = 0
    for rt in range(len(sequence)):
        sumV += sequence[rt]
        if sumV == k:
            check(lt, rt)
        while sumV >= k:
            sumV -= sequence[lt]
            lt += 1
            if sumV == k:
                check(lt, rt)

    return answer
