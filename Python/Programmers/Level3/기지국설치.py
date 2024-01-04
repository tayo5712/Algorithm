import math

def solution(n, stations, w):
    answer = 0
    st = 1
    for station in stations:
        distance = (station - w - 1) - st + 1
        answer += math.ceil(distance / (2 * w + 1))
        st = station + w + 1        
        
    if st <= n:
        answer += math.ceil((n - st + 1) / (2 * w + 1))
    
    return answer
