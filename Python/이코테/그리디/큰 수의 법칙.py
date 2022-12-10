N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
first = arr[-1]
second = arr[-2]

# for _ in range(M):
#     sum += first
#
# for _ in range(K, M, K):
#     sum -= first
#     sum += second
#
# print(sum)

count = int(M / (K + 1)) * K + M % (K + 1)

sum += (count) * first
sum += (M - count) * second
print(sum)