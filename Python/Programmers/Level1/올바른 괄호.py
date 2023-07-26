def solution(s):
    answer = True
    st = []
    for ss in s:
        if ss == "(":
            st.append(ss)
        else:
            if len(st) < 1:
                answer = False
                break
            ch = st.pop()
            if ch != '(':
                answer = False
                break
    if len(st) > 0:
        answer = False

    return answer