def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            print(i, j)
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
