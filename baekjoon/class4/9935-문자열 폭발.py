import sys
input = sys.stdin.readline

arr = input().rstrip()
bomb = list(input().rstrip())

result = []

for i in range(len(arr)):
    result.append(arr[i])   # result에 원래 arr을 하나씩 추가해줌
    if len(result) >= len(bomb) and result[-len(bomb):] == bomb:    # result의 뒷 부분이 bomb과 같으면 bomb의 길이만큼 pop
        for _ in range(len(bomb)):
            result.pop()

if result:
    print(*result, sep='')
else:
    print('FRULA')





# replace 시간 초과
# arr = input().rstrip()
# bomb = input().rstrip()
#
# while True:
#     if bomb in arr:
#         arr = arr.replace(bomb, "")
#     else:
#         break
#
# if arr:
#     print(arr)
# else:
#     print('FRULA')