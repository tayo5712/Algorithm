T = int(input())
for tc in range(1, T+1):
    n = int(input())
    st = {}
    students = list(map(int, input().split()))
    for student in students:
        if student not in st:
            st[student] = 1
        else:
            st[student] += 1
    maxV = 0
    maxK = 0
    for key, value in st.items():
        if value > maxV:
            maxV = value
    for key, value in st.items():
        if value == maxV and key > maxK:
            maxK = key

    print(f'#{tc} {maxK}')
