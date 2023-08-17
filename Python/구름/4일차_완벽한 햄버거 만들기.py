# https://level.goorm.io/exam/195686/%EC%99%84%EB%B2%BD%ED%95%9C-%ED%96%84%EB%B2%84%EA%B1%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1
# 구름 챌린지 4일차

n = int(input())
flag = True
arr = list(map(int, input().split()))
index = arr.index(max(arr))
left_arr = arr[:index]
right_arr = arr[index + 1:]
for i in range(1, len(left_arr)):
    if left_arr[i - 1] > left_arr[i]:
        flag = False
        break
if flag:
    for i in range(1, len(right_arr)):
        if right_arr[i - 1] < right_arr[i]:
            flag = False
            break
print(sum(arr)) if flag else print(0)
