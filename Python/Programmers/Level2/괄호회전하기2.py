def is_valid(ss):
    stack = []
    for word in ss:
        if len(stack) == 0:
            stack.append(word)
        else:
            if (stack[-1] == "[" and word == "]") or (stack[-1] == "{" and word == "}") or (stack[-1] == "(" and word == ")"):
                stack.pop()
            else:
                stack.append(word)
    if stack:
        return False
    else:
        return True

def solution(s):
    pos = 0
    answer = 0
    while pos < len(s):
        tmp = s[pos::] + s[:pos]
        if is_valid(tmp):
            answer += 1
        pos += 1
    return answer
