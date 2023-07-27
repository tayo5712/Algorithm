answer = 0

def DFS(numbers, n, sumV, target):
    global answer
    if n == len(numbers):
        if sumV == target:
            answer += 1
        return
    DFS(numbers, n+1, sumV+numbers[n], target)
    DFS(numbers, n+1, sumV-numbers[n], target)

def solution(numbers, target):
    DFS(numbers, 0, 0, target)
    return answer

# DFS 더하거나 빼거나