answer = []
def hanoi(n, st, ed, sub):
    if n == 1:
        answer.append([st, ed])
        # 원반이 한개일 경우 시작기둥에서 목표기둥으로 옮겨주면 된다.
        return
    hanoi(n-1, st, sub, ed)
    # 시작기둥에 있는 (n-1)개의 원반들을 보조기둥으로 옮기기
    answer.append([st, ed])
    # (n-1)개 원반을 전부다 옮겼으면 남은 원반을 시작기둥에서 목표기둥으로 옮기기
    hanoi(n-1, sub, ed, st)
    # 보조 기둥에 있는 원반들을 목표기둥으로 옮기기

def solution(n):
    hanoi(n, 1, 3, 2)
    return answer