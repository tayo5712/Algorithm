def count_ways(N, Vip):
    DP = [0] * (N + 1)
    DP[0] = 1
    DP[1] = 1

    for i in range(2, N + 1):
        DP[i] = DP[i - 1] + DP[i - 2]

    total_ways = 1
    prev_vip_seat = 0

    for vip_seat in Vip:
        total_ways *= DP[vip_seat - prev_vip_seat - 1]
        prev_vip_seat = vip_seat

    total_ways *= DP[N - prev_vip_seat]

    return total_ways

N = int(input())
M = int(input())
Vip = []

for _ in range(M):
    Vip.append(int(input()))

result = count_ways(N, Vip)
print(result)
