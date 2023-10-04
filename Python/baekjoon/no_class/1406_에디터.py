left_stack = list(input())
right_stack = []
M = int(input())
for _ in range(M):
    command = input().rstrip()
    if command == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == 'B':
        if left_stack:
            left_stack.pop()
    else:
        left_stack.append(command[-1])
left_stack.extend(reversed(right_stack))
print(''.join(left_stack))