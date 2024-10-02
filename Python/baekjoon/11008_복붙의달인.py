n = int(input())

for _ in range(n):
    s, word = map(str, input().split())
    cnt = 0
    cnt = s.count(word)
    replaced_s = s.replace(word, "")
    print(cnt + len(replaced_s))
