sound = input()
visited = [0] * len(sound)
answer = 0
correct = 0
w = ['q', 'u', 'a', 'c', 'k']
if len(sound) % 5 != 0:
    print(-1)
else:
    for i in range(len(sound)-4):
        if not visited[i] and w[0] == sound[i]:
            idx = 1
            visited[i] = 1
            cnt = 1
            match = 0
            for j in range(i + 1, len(sound)):
                if not visited[j] and w[idx] == sound[j]:
                   visited[j] = 1
                   idx = (idx + 1) % 5
                   if idx == 0:
                       match += 1
            if match:
                answer += 1
                correct += match
    if correct == len(sound) // 5:
        print(answer)
    else:
        print(-1)
