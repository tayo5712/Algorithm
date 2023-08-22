def combi(depth, st):
    global com, combi_lst
    if depth == 2:
        combi_lst.append((com[0], com[1]))
    else:
        for i in range(st, n):
            com[depth] = i
            combi(depth + 1, i + 1)


n = int(input())
words = input()
combi_lst = []
mySet = set()
com = [0, 0]
combi(0, 1)
answer = 0
for st, ed in combi_lst:
    mySet.add(words[:st])
    mySet.add(words[st:ed])
    mySet.add(words[ed:])

myList = sorted(list(mySet))
for st, ed in combi_lst:
    tmp = 0
    tmp += myList.index(words[:st]) + 1
    tmp += myList.index(words[st:ed]) + 1
    tmp += myList.index(words[ed:]) + 1
    answer = max(answer, tmp)

print(answer)

