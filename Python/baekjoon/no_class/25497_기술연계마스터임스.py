n = int(input())
skills = list(input())
answer = 0
stack = []

for skill in skills:
    if skill.isdigit():
        answer += 1
    else:
        if skill == 'L':
            stack.append(skill)
        elif skill == 'S':
            stack.append(skill)
        elif skill == 'R':
            if stack and stack[-1] == 'L':
                stack.pop()
                answer += 1
            else:
                stack.append(skill)
        elif skill == 'K':
            if stack and stack[-1] == 'S':
                stack.pop()
                answer += 1
            else:
                stack.append(skill)
print(answer)
