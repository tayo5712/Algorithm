import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        yMax = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        yMin = 0 if x >= r1 else math.ceil(math.sqrt(r1 ** 2 - x ** 2))
        answer += yMax - yMin + 1
    return answer * 4

# 2중 for문 시간초과
# x값에서 최대의 가능한 y좌표와 최소의 y좌표를 구해서 값 계산 * 4
# 피타고라스의 정리 x^2 + y^2 = r^2