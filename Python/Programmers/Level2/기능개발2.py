def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    idx = 0
    while idx < n:
        today = 0
        for i in range(n):
            if i >= idx:
                progresses[i] += speeds[i]
                if progresses[idx] >= 100 and progresses[i] >= 100:
                    today += 1
                    idx += 1
        if today:
            answer.append(today)

    return answer
