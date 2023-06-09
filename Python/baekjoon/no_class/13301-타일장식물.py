n = int(input())
dp = [0, 4, 6, 10]
for i in range(4, n+1):
    nDp = dp[i-2] + dp[i-1]
    dp.append(nDp)

print(dp[n])

# n = int(input())
# line = [0, 1, 1]
# dp = [0, 4, 6]
#
# for i in range(3, n + 1):
#     nextLine = line[i - 2] + line[i - 1]
#     line.append(nextLine)
#     a = dp[i - 1] + 2 * nextLine
#     dp.append(a)
#
# print(dp[n])