for tc in range(1, 11):
    n, s = input().split()
    lst = [s[0]]
    for i in range(1, int(n)):
        if len(lst):
            if lst[-1] == s[i]:
                lst.pop()
            else:
                lst.append(s[i])
        else:
            lst.append(s[i])
    print(f"#{tc} {''.join(lst)}")
