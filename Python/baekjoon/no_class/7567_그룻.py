bowls = list(input())
stack = []
cnt = 0
for bowl in bowls:
    if len(stack) == 0:
        cnt += 10
    elif stack[-1] == bowl:
        cnt += 5
    else:
        cnt += 10
    stack.append(bowl)
print(cnt)