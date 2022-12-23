n = int(input())
people = list(int(input()) for _ in range(n))
stack = []
result = 0

for person in people:
    while stack and stack[-1][0] < person:  # 현재 사람이 스택top에 있는 사람 보다 크면 현재 사람 뒤에 오는 사람은 어차피 현재 사람 앞에 오는 사람을 볼 수 없음
        result += stack.pop()[1]    # 현재사람의 키보다 크거나 같은 사람이 나올 때까지 pop하면서 결과 값에 더해 줌

    if stack:   # 스택이 있으면
        if stack[-1][0] == person:  # 스택의 top이 현재 사람의 키와 같으면 키가 같은 사람끼리는 전부 볼 수 있으므로 pop하면서 연속 횟수를 더해나감
            cnt = stack.pop()[1]
            result += cnt
            if stack:  
                result += 1     # 앞 사람과는 무조건 볼 수 있으므로 +1
            stack.append([person, cnt + 1]) # 연속 횟수에 1을 더해나감
        else:
            result += 1     # 앞 사람과는 무조건 볼 수 있으므로 +1
            stack.append([person, 1])
    else:   # 스택이 비었으면 현재 사람을 추가 (현재사람의 키, 현재사람의 키의 연속횟수)
        stack.append([person, 1])

print(result)