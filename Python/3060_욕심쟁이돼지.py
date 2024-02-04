tc = int(input())
for _ in range(tc):
    n = int(input())
    feed = sum(list(map(int, input().split())))
    day = 1
    while n >= feed:
        feed *= 4
        day += 1
    print(day)
    
