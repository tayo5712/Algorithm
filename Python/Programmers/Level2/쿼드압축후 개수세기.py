answer = [0, 0]
def cur(arr, x1, x2, y1, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[x1][y1] != arr[i][j]:
                cur(arr, x1, (x1 + x2) // 2, y1, (y1 + y2) // 2)
                cur(arr, (x1 + x2) // 2, x2, y1, (y1 + y2) // 2)
                cur(arr, x1, (x1 + x2) // 2, (y1 + y2) // 2, y2)
                cur(arr, (x1 + x2) // 2, x2, (y1 + y2) // 2, y2)
                return

    if arr[x1][y1] == 0:
        answer[0] += 1
    else:
        answer[1] += 1


def solution(arr):
    cur(arr, 0, len(arr), 0, len(arr))

    return answer

# 분할 정복
# 해당 사분면 안이 전부 같은 숫자가 아니라면 4 사분면으로 쪼개서 재귀호출