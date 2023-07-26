def solution(brown, yellow):
    ab = brown + yellow
    for b in range(2, int(ab/2)):
        if ab % b == 0:
            a = ab // b
            if a >= b and a * 2 + b * 2 - 4 == brown:
                return [a, b]