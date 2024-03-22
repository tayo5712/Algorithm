def solution(n, times):
    
    lt = min(times)
    rt = max(times) * n
    answer = rt
    while lt <= rt:
        mid = (lt + rt) // 2
        total = 0
        for t in times:
            total += mid // t
        
        if total >= n:
            answer = min(answer, mid)
            rt = mid - 1
        else:
            lt = mid + 1
        
    return answer
