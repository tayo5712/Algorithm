from itertools import combinations

N, K = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(N)]

Min_Range = float('inf')

for S in combinations(range(N), K):
    Max_Range = 0

    for i in range(N):
        Home = H[i]
        Shelter = [H[S[a]] for a in range(K)]
        min_Range = float('inf')
        
        for j in Shelter:
            Range = abs(Home[0] - j[0]) + abs(Home[1] - j[1])
            min_Range = min(min_Range, Range)

        Max_Range = max(Max_Range, min_Range)

    Min_Range = min(Min_Range, Max_Range)

print(Min_Range)
