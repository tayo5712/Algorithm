n = int(input())
m = int(input())
target = list(map(int, input().split()))
score = [0] * n
for i in range(m):
    a = list(map(int, input().split()))
    for j in range(n):
        if target[i] == a[j]:
            score[j] += 1
        else:
            score[target[i] - 1] += 1
for i in score:
    print(i)