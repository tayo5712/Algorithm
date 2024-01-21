def solution(today, terms, privacies):
    answer = []
    today = today.split(".")
    terms_dict = dict()
    for term in terms:
        kind, month = term.split()
        terms_dict[kind] = int(month) * 28
    
    for i in range(len(privacies)):
        d, kind = privacies[i].split()
        date = d.split(".")
        
        differ = 0
        # 년
        differ += (int(today[0]) - int(date[0])) * 12 * 28
        # 월
        differ += (int(today[1]) - int(date[1])) * 28
        # 일
        differ += (int(today[2]) - int(date[2]))
        
        if terms_dict[kind] <= differ:
            answer.append(i+1)
        
    return answer
