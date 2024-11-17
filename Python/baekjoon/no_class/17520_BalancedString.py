N = int(input())
DP = [0] * (N + 1)
DP[1] = 2
for i in range(2, N + 1):
    if (i % 2):
        DP[i] = (DP[i-1] * 2) % 16769023
    else:
        DP[i] = DP[i - 1]
print(DP[N])
