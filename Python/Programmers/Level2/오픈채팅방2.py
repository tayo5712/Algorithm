def solution(records):
    answer = []
    name = {}
    
    for record in records:
        tmp = record.split()
        if tmp[0] == "Enter":
            name[tmp[1]] = tmp[2]
        elif tmp[0] == "Change":
            name[tmp[1]] = tmp[2]
    
    for record in records:
        tmp = record.split()
        if tmp[0] == "Enter":
            answer.append(name[tmp[1]] + "님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            answer.append(name[tmp[1]] + "님이 나갔습니다.")
            
    return answer
