def solution(participant, completion):
    answer = ''
    part = {}
    for p in participant:
        if p not in part:
            part[p] = 0
        part[p] += 1
    for com in completion:
        part[com] -= 1
    for k, v in part.items`():
        if v == 1:
            answer = k
            break
    return answer
