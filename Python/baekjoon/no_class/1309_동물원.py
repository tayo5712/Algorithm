N = int(input())

cache = [[0]*3 for _ in range(N)]
cache[0] = [1, 1, 1]

for i in range(1, N):
    cache[i][0] = (cache[i-1][2] + cache[i-1][1]) % 9901
    cache[i][1] = (cache[i-1][2] + cache[i-1][0]) % 9901
    cache[i][2] = (cache[i-1][0] + cache[i-1][1] + cache[i-1][2]) % 9901

print(sum(cache[N-1]) % 9901)