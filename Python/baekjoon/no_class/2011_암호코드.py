arr = input()
if arr[0] == "0":
    print(0)
else:
    n = len(arr)
    arr = "0" + arr
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        if arr[i] != "0":
            dp[i] += dp[i-1]
        if i > 1 and 10 <= int(arr[i-1:i+1]) <= 26:
            dp[i] += dp[i-2]

    print(dp[-1] % 1000000)
