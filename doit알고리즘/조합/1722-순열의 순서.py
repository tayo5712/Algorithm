# 메모리 초과
# def perm(k):
#     global answer
#     if k == n:
#         num = []
#         for i in range(n):
#             num.append(a[result[i]])
#         answer.append(num)
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = 1
#             result[k] = i
#             perm(k+1)
#             visited[i] = 0
#
# n = int(input())
# arr = list(map(int, input().split()))
# a = list(range(1, n+1))
# result = [0] * n
# visited = [0] * n
# answer = []
# perm(0)
#
# if arr[0] == 1:
#     print(*answer[arr[1]-1])
# else:
#     print(answer.index(arr[1:])+1)