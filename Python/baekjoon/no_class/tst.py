def solution(n, colors):
    # 각 색깔 블록의 개수를 세기 위한 딕셔너리 생성
    count = {}
    for color in colors:
        if color not in count:
            count[color] = 0
        count[color] += 1

    # 각 색깔 블록을 순회하며 가능한 최대 점수 계산
    max_score = 0
    for color, num_blocks in count.items():
        max_score += num_blocks ** 2

    return max_score

# 예시 입력
n = 10
colors = [1, 1, 2, 2, 2, 3, 3, 3, 2, 2]

# 최대 점수 계산
result = solution(n, colors)
print(result)