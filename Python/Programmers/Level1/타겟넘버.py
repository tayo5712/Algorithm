cnt = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(idx, sumV, numbers, target):
        global cnt
        if idx == n:
            if sumV == target:
                cnt += 1
            return
        else:
            dfs(idx + 1, sumV + numbers[idx], numbers, target)
            dfs(idx + 1, sumV - numbers[idx], numbers, target)
    
    dfs(0, 0, numbers, target)
    return cnt
