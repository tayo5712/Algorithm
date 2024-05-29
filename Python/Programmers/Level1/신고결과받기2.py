def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    user = dict()
    dic = dict()
    
    for idx in range(len(id_list)):
        user[id_list[idx]] = idx 
    
    for s in report:
        a, b = s.split()
        if b not in dic:
            dic[b] = set()
        dic[b].add(a)
    
    for key, value in dic.items():
        if len(value) >= k:
            for u in value:
                answer[user[u]] += 1
    
    return answer
