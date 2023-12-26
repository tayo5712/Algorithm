from copy import deepcopy

def solution(want, number, discount):
    answer = 0
    need = {}
    for i in range(len(want)):
        if want[i] not in need:
            need[want[i]] = 0
        need[want[i]] += number[i]

    total = sum(number)
    flag = True
    start = 0
    while flag:
        need2 = deepcopy(need)
        s = 0
        for i in range(start, start + total):
            if discount[i] in need and need2[discount[i]] > 0:
                need2[discount[i]] -= 1
                s += 1
        if s == total:
            answer += 1

        start += 1
        if (start + total) > len(discount):
            flag = False
    return answer
