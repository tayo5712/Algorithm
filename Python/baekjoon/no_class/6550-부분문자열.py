import sys

input = sys.stdin.readline

while True:
    st = input().rstrip()
    if not st:
        break
    s, t = st.split()
    flag = 0
    idx = 0

    for i in range(len(t)):
        if t[i] == s[idx]:
            idx += 1
            if idx == len(s):
                flag = 1
                break

    if flag == 1:
        print('Yes')
    else:
        print('No')