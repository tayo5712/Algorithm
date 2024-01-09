def solution(numbers):
    answer = str(int("".join(sorted([str(i) for i in numbers], key = lambda x : x * 3, reverse = True))))
    return answer
