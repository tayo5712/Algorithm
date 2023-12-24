def solution(s):
    answer = 0
    stack = []
    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
        else:
            if stack[-1] == letter:
                while stack and stack[-1] == letter:
                        stack.pop()
            else:
                stack.append(letter)
    if not stack:
        answer = 1
    return answer