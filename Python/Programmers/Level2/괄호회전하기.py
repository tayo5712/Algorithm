def is_valid(ss):
    stack = []
    for word in ss:
        if len(stack) == 0:
            stack.append(word)
        else:
            if (stack[-1] == "[" and word == "]") or (stack[-1] == "(" and word == ")") or (stack[-1] == "{" and word == "}"):
                stack.pop()
            else:
                stack.append(word)
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    pos = 0
    while pos < len(s):
        if is_valid(s[pos:len(s)]+s[0:pos]):
            answer += 1
        pos += 1
    return answer