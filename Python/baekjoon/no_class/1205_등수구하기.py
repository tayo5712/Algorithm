n, my_score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    ranking = list(map(int, input().split()))
    if n == p and ranking[-1] >= my_score:
        print(-1)
    else:
        rank = 0
        for score in ranking:
            rank += 1
            if my_score >= score:
                print(rank)
                break
        else:
            print(n+1)
