def solution(brown, yellow):
    ab = brown + yellow
    for b in range(3, ab // 2):
        a = ab // b
        if ab % b == 0 and (a - 2) * 2 + (b * 2) == brown:
            return [a, b]
