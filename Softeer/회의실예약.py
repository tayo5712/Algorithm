import sys

input = sys.stdin.readline

rooms = dict()
n, m = map(int, input().split())
for _ in range(n):
    room_name = input().rstrip()
    rooms[room_name] = [0] * 18 + [1] # 0 ~ 18 인덱스 편리하게 쓰려고

for _ in range(m):
    room_name, start, end = input().split()
    for i in range(int(start), int(end)):     
        rooms[room_name][i] = 1

rooms = dict(sorted(rooms.items()))

index = 1
for key, value in rooms.items():
    st = 0
    times = []
    for i in range(9, 19):
        if value[i] == 0:
            if st == 0:
                st = i
        else:
            if st != 0:
                a, b = str(st), str(i)
                if len(a) == 1:
                    a = "0" + a
                if len(b) == 1:
                    b = "0" + b
                times.append(a + "-" + b)
                st = 0
            
    print(f'Room {key}:')
    if len(times):
        print(f'{len(times)} available:')
        for i in range(len(times)):
            print(times[i])
    else:
        print("Not available")
    if index != n:
        print("-----")
    index += 1
