def solution(survey, choices):
    character = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    comb = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    answer = ''
    for i in range(len(survey)):
        a = survey[i][0]
        b = survey[i][1]
        score = choices[i]
        if score < 4:
            character[a] += abs(4-score)
        elif score > 4:
            character[b] += score-4
    for i in range(4):
        answer += comb[i][0] if character[comb[i][0]] >= character[comb[i][1]] else comb[i][1]
    
    return answer
