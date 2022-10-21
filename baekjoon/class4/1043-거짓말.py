n, m = map(int, input().split())
who = list(map(int, input().split()))
truth_list = [0] * (n+1)
if who[0]:  # 진실을 아는 사람이 있는 경우
    truth = who[1:]   # 처음 진실을 아는 사람들의 리스트
    for p in truth:
        truth_list[p] = 1   # 진실을 아는 사람 체크하기

    cnt = 0
    all_parties = []
    for _ in range(m):
        participants = list(map(int, input().split()))[1:]
        all_parties.append(participants)    # 모든 파티를 한 리스트에 담기

    for _ in range(m):  # 뒤에서 진실을 들었던 사람이 거짓말을 들었던 사람에게 알려 줄 수 있으므로 파티 개수 만큼 반복 한다.
        for party in all_parties:
            for people in party:
                if truth_list[people] == 1: # 만약 그 파티에 진실을 아는 사람이 있다면 그 파티 전부 진실 처리
                    for people in party:
                        truth_list[people] = 1
                    break

    for party in all_parties:
        for people in party:    # 파티에 진실쟁이가 있으면 넘어감
            if truth_list[people] == 1:
                break
        else:   # 없으면 거짓말 치기
            cnt += 1
    print(cnt)

else:   # 진실을 아는 사람이 0명인 경우 파티 개수 만큼이 최대값
    print(m)




'''
set으로 푼거
n, m = map(int, input().split())
who = list(map(int, input().split()))
if who[0]:
    truth = set(who[1:])
    parties = []
    for _ in range(m):
        parties.append(set(list(map(int, input().split()))[1:]))

    for _ in range(m):
        for party in parties:
            if party & truth:
                truth = truth.union(party)

    cnt = 0
    for party in parties:
        if party & truth:
            continue
        cnt += 1
    print(cnt)

else:
    print(m)
'''




