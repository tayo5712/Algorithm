def solution(numbers):
    answer = "".join(sorted((str(i) for i in numbers), key = lambda x : x * 3, reverse = True))
    return str(int(answer))