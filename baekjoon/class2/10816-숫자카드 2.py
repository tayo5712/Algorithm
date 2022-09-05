import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

# 시간 초과
# for i in check:
#     print(num.count(i), end = ' ')

num_dict = {}
for i in num:
    if i not in num_dict:           # 사전에 담기
        num_dict[i] = 1             # 해당 값이 없으면 추가
    else:
        num_dict[i] += 1            # 있으면 value값에 1추가

for j in check:
    if j not in num_dict:           # check의 요소가 딕셔너리에 없으면 0 출력
        print(0, end = ' ')
    else:                           # 있으면 해당 value값 출력
        print(num_dict[j], end = ' ')