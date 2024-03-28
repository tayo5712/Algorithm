tc = int(input())
for _ in range(tc):
    s = input()
    k, maxV, minV = int(input()), 0, len(s)
    words = dict()
    for i in range(len(s)):
        if s[i] not in words:
            words[s[i]] = []
        words[s[i]].append(i)

    for key, value in words.items():
        if len(value) >= k:
            lt = 0
            for rt in range(k - 1, len(value)):
                maxV = max(maxV, value[rt] - value[lt] + 1)
                minV = min(minV, value[rt] - value[lt] + 1)
                lt += 1

    print(minV, maxV) if maxV else print(-1)
