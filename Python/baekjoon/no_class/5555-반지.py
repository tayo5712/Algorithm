word = input()
n = int(input())
cnt = 0
for _ in range(n):
    question = input()
    question += question
    if word in question:
        cnt += 1
print(cnt)