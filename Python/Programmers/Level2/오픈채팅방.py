def solution(records):
    answer = []
    tmpL = []
    tmpD = {}
    for record in records:
        record = record.split(" ")
        if record[0] == "Enter":
            tmpD[record[1]] = record[2]
            tmpL.append(record)
        elif record[0] == "Leave":
            tmpL.append(record)
        else:
            tmpD[record[1]] = record[2]

    for record in tmpL:
        if record[0] == "Enter":
            chat = tmpD[record[1]] + "님이 들어왔습니다."
        else:
            chat = tmpD[record[1]] + "님이 나갔습니다."
        answer.append(chat)

    return answer

# 딕셔너리에 유저아이디를 키값으로 닉네임을 넣어뒀다가 유저아이디를 기준으로 닉네임이 변경되면 딕셔너리 값을 바꿔줌