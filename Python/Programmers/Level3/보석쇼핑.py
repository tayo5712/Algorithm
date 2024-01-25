def solution(gems):
    answer = []
    set_gems = set(gems)
    set_n = len(set_gems)
    
    min_length = 100000
    
    left = right = 0
    
    jdict = dict()
    
    while left <= right and right < len(gems):
        
        if gems[right] not in jdict:
            jdict[gems[right]] = 1
        else:
            jdict[gems[right]] += 1
            
        while len(jdict) == set_n:
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right + 1]
                
            jdict[gems[left]] -= 1
            if jdict[gems[left]] == 0:
                jdict.pop(gems[left])
            left += 1
            
        right += 1
    return answer
