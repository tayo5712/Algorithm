import sys
input = sys.stdin.readline

total = 0
answer = []
dic = {}
while True:
    word = input().rstrip()
    if not word:
        break
    else:
        total += 1
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
sdic = dict(sorted(dic.items()))
for word in sdic:
    cnt = sdic[word]
    per = ((cnt / total) * 100)
    print(f'{word} {per:.4f}')