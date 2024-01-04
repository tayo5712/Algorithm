def solution(k, tangerine):
    answer = 0
    bucket = dict()
    for t in tangerine:
        if t not in bucket:
            bucket[t] = 0
        bucket[t] += 1
    
    bucket = sorted(bucket.items(), key = lambda x : -x[1])
    
    for i in range(len(bucket)):
        if k > 0:
            k -= bucket[i][1]
            answer += 1
        else:
            break
    
    return answer
