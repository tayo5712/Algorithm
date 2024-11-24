def mid_score():
    scores = list(map(int, input().split()))
    len_score = len(scores)

    _dict = {}
    for i in range(m):
        data = list(map(str, input().split()))
        num, arr = data[0], data[1:]

        _dict[num] = _dict.setdefault(num, 0)
        for j in range(len_score):
            if arr[j] == 'O':
                _dict[num] += scores[j]

    min_student = 100001
    max_val = max(_dict.values())
    for k, v in _dict.items():
        if v == max_val:
            min_student = min(min_student, int(k))

    print(min_student, max_val)


n, m = map(int, input().split())
mid_score()
