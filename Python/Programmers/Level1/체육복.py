def solution(n, lost, reserve):
    total = n
    for i in range(1, n + 1):
        if i in lost:
            if i in reserve:
                lost.remove(i)
                reserve.remove(i)
    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                reserve.remove(i - 1)
            elif i + 1 in reserve:
                reserve.remove(i + 1)
            else:
                total -= 1

    return total
