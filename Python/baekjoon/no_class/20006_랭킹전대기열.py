p, m = map(int, input().split())

players = list(input().split() for _ in range(p))
rooms = [[] for _ in range(300)]
for player in players:
    for room in rooms:
        if len(room) == 0:
            room.append(player)
            break
        elif int(room[0][0]) - 10 <= int(player[0]) <= int(room[0][0]) + 10 and len(room) < m:
            room.append(player)
            break
for room in rooms:
    if len(room) == 0:
        break
    room.sort(key = lambda x : x[1])
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in room:
        print(player[0], player[1])
