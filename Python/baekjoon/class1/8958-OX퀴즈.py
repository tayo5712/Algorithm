for _ in range(int(input())):
    arr = input()
    score = 0
    cnt = 0
    for a in arr:
        if a == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
