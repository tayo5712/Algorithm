import sys
input = sys.stdin.readline
N, M, L, K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]
answer = K
for i in range(K):
    for j in range(K):
        cnt = 0
        for star in stars: # 두별의 기준으로 무게중심을 잡는다.
            if stars[i][0] <= star[0] <= stars[i][0] + L and stars[j][1] <= star[1] <= stars[j][1] + L:
                cnt += 1
        answer = min(answer, K-cnt)
print(answer)
