def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sumV = 0
            for k in range(len(arr1[0])):
                sumV += arr1[i][k] * arr2[k][j]
            answer[i].append(sumV)
    return answer