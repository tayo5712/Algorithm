def solution(plans):
    answer = []
    wait = []
    plans.sort(key=lambda x: x[1])
    for plan in plans:
        hour, minute = map(int, plan[1].split(":"))
        calTime = hour * 60 + minute
        plan[1] = calTime
        plan[2] = int(plan[2])

    for i in range(len(plans)):
        if i + 1 == len(plans):
            # 마지막 과제일 경우 끝내고 남은 과제 차례로 끝내기
            answer.append(plans[i][0])
            while wait:
                answer.append(wait.pop()[0])
        else:
            nowTime = plans[i][1] + plans[i][2]
            if nowTime <= plans[i + 1][1]:
                # 현재 과제(시작시간 + 끝시간)이 다음 과제(시작 시간)보다 작거나 같을경우 (완료)
                answer.append(plans[i][0])
                if wait and nowTime < plans[i + 1][1]:
                    # 자투리 시간에 전에 못 끝낸 과제 끝내기
                    while wait and True:
                        remain = wait.pop()
                        if nowTime + remain[1] <= plans[i + 1][1]:
                            # 남은 과제가 다음 과제시작 시간전에 끝날경우
                            answer.append(remain[0])
                            nowTime += remain[1]
                        else:
                            # 남은 과제가 다음 과제시작 전에 못 끝날경우 가능한 시간만큼 남은 시간을 빼서 다시 wait에 넣어준다
                            wait.append((remain[0], remain[1] - (plans[i + 1][1] - nowTime)))
                            break
            else:
                # 현재 과제가 다음 과제전에 못 끝날경우 남은 시간만큼 빼서 wait에 넣어준다.
                wait.append((plans[i][0], nowTime - plans[i + 1][1]))

    return answer