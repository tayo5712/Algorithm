T = int(input())
for tc in range(T):
    n = int(input())
    people = list(list(map(int, input().split())) for _ in range(n))
    people.sort(key=lambda x: (x[0], x[1]))
    minS = 100001
    answer = 0
    for p in people:
        if p[1] < minS:
            answer += 1
            minS = p[1]
    print(answer)