n = int(input())
words = list(input() for _ in range(n))
words_set = set(words)
st = ''
ed = ''
m = int(input())
if n != 1:
    for i in range(n):
        if words[i] == '?':
            if i == 0:
                ed = words[i+1][0]
            elif i == n-1:
                st = words[i - 1][-1]
            else:
                st = words[i - 1][-1]
                ed = words[i+1][0]
    for i in range(m):
        w = input()
        if st != '' and ed != '':
            if w[0] == st and w[-1] == ed and w not in words_set:
                print(w)
                break
        elif st != '' and w not in words_set:
            if w[0] == st:
                print(w)
                break
        else:
            if w[-1] == ed and w not in words_set:
                print(w)
                break
else:
    print(input())
