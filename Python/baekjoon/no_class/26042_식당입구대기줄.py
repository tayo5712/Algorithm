n = int(input())
stack = []
maxs = [0,0]
for _ in range(n):
    info = list(map(int,input().split()))
    if len(info) == 1:
        stack.pop(0)
    else:
        stack.append(info[1])

    if maxs[0] < len(stack):
        maxs[0] = len(stack)
        maxs[1] = stack[-1]
    elif maxs[0] == len(stack):
        maxs[1] = min(maxs[1],stack[-1])

print(maxs[0],maxs[1])
