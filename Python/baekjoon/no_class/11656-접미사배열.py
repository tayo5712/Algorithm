n = input()
answer = []
for i in range(len(n)):
    answer.append(n[i::])
for word in sorted(answer):
    print(word)