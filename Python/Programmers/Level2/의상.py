def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] not in dict:
            dict[cloth[1]] = 0
        dict[cloth[1]] += 1
    for key, value in dict.items():
        answer *= value + 1
    return answer - 1
