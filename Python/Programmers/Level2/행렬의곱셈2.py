def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for k in range(len(arr2[0])):
            s = 0
            for j in range(len(arr2)):
                s += arr1[i][j] * arr2[j][k]
            tmp.append(s)
        answer.append(tmp)
        
    return answer
    
