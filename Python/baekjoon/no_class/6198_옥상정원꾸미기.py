n = int(input())
stack = []
result = 0
for _ in range(n):
    building = int(input())
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)
    result += len(stack) - 1
print(result)
