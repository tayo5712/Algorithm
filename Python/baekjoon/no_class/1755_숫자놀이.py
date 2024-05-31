n, m = map(int, input().split())
answer = []

word = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}

for i in range(n, m + 1):
    s = str(i)
    first = word[s[0]]
    if len(s) > 1:
        first += word[s[1]]
    answer.append((first, i))

answer = sorted(answer, key = lambda x : x[0])
for i in range(len(answer)):
    print(answer[i][1], end = " ")
    if (i + 1) % 10 == 0:
        print()
