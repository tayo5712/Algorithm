num = input()

if "0" not in num:
    print(-1)
else:
    numSum = 0
    for n in num:
        numSum += int(n)
    if numSum % 3 != 0:
        print(-1)
    else:
        answer = sorted(num, reverse = True)
        print(''.join(answer))


# def DFS(L):
#     global result
#     global flag
#     if not flag:
#         return
#     if L == n:
#         tmp = int(''.join(answer))
#         if tmp % 30 == 0:
#             result = tmp
#             flag = False
#     else:
#         for i in range(n):
#             if not ch[i]:
#                 ch[i] = 1
#                 answer[L] = arr[i]
#                 DFS(L + 1)
#                 ch[i] = 0
#
#
# arr = list(input())
# arr.sort(reverse=True)
# n = len(arr)
#
# answer = [0] * n
# result = ""
# flag = True
# ch = [0] * n
# DFS(0)
#
# if result == "":
#     print(-1)
# else:
#     print(result)