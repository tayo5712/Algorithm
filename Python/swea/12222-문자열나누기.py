T = int(input())
for tc in range(1, T + 1):
    words = input()
    cur = ""
    pre = ""
    answer = []
    for word in words:
        cur += word
        if cur != pre:
            answer.append(cur)
            pre = cur
            cur = ""
    print(f'#{tc} {len(answer)}')