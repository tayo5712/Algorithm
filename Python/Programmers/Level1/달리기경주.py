def solution(players, callings):
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
    for call in callings:
        r = rank[call] # 불린 사람의 현재 등수
        # 딕셔너리 값 바꾸기
        rank[call] = rank[players[r - 1]]
        rank[players[r - 1]] = r
        # 배열 값 바꾸기
        call_people = players[r]
        players[r] = players[r - 1]
        players[r - 1] = call_people
    return players
