def solution(numbers, hand):
    pos = {"1" : (0, 0), "2" : (0, 1), "3" : (0, 2), "4" : (1, 0), "5" : (1, 1), "6" : (1, 2), "7" : (2, 0), "8" : (2, 1), "9" : (2, 2), "*" : (3, 0), "0" : (3, 1), "#" : (3, 2)}
    answer = ''
    lp = pos["*"]
    rp = pos["#"]
    for number in numbers:
        
        number = str(number)
        if number in ["1", "4", "7"]:
            answer += 'L'
            lp = pos[number]
        elif number in ["3", "6", "9"]:
            answer += 'R'
            rp = pos[number]
        else:
            ld = abs(pos[number][0] - lp[0]) + abs(pos[number][1] - lp[1])
            rd = abs(pos[number][0] - rp[0]) + abs(pos[number][1] - rp[1])
            if ld > rd:
                answer += 'R'
                rp = pos[number]
            elif ld < rd:
                answer += 'L'
                lp = pos[number]
            else:
                if hand == "left":
                    answer += 'L'
                    lp = pos[number]
                else:
                    answer += 'R'
                    rp = pos[number]
    return answer
