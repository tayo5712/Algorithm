
n = int(input())
result = 0

for i in range(n):
    line = input()
    stack = [line[0]]

    for j in range(1, len(line)):
        if (len(stack) == 0):
            stack.append(line[j])

        else:
            top = stack[-1]
            if line[j] == top:
                stack.pop()
            else:
                stack.append(line[j])

    if (len(stack) == 0):
        result += 1

print(result)
