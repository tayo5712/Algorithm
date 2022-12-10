n = int(input())
for _ in range(n):
    floor = int(input())
    door = int(input())

    f0 = list(range(1, door + 1))   # 0층에 사람 수 리스트
    for _ in range(floor):                  # 층 수 만큼 반복
        for i in range(1, door):            # 층 별 각 호실 인원 수 를 갱신
            f0[i] += f0[i-1]

    print(f0[-1])   # 가장 마지막 수가 해당 층, 해당 호수에 사는 인원
