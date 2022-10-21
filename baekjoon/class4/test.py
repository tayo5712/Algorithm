n, m = map(int, input().split())
who = list(map(int, input().split()))
truth_list = [0] * (n+1)
if who[0]:
    truth = who[1:]
    for p in truth:
        truth_list[p] = 1

    cnt = 0
    all_parties = []
    for _ in range(m):
        participants = list(map(int, input().split()))[1:]
        all_parties.append(participants)

    for _ in range(m):
        for party in all_parties:
            for people in party:
                if truth_list[people] == 1:
                    for people in party:
                        truth_list[people] = 1
                    break

    for party in all_parties:
        for people in party:
            if truth_list[people] == 1:
                break
        else:
            cnt += 1
    print(cnt)

else:
    print(m)




