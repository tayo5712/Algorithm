def solution(n):
    def promising(index, arr):
        for i in range(index):
            if arr[i] == arr[index] or abs(arr[index] - arr[i]) == index - i:
                return False
        return True

    def nqueen(index, arr):
        answer = 0
        if index >= n:
            return 1
        else:
            for i in range(n):
                arr[index] = i
                if promising(index, arr):
                    answer += nqueen(index + 1, arr)
        return answer

    lst = [0] * n

    return nqueen(0, lst)


