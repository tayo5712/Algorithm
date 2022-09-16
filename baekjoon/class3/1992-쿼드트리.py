def divide(sti, stj, n):
    global st
    start = arr[sti][stj]
    for i in range(sti, sti + n):
        for j in range(stj, stj + n):
            if start != arr[i][j]:
                st.append('(')
                for x in range(2):
                    for y in range(2):
                        divide(sti + x * (n//2), stj + y * (n//2), n//2)
                st.append(')')
                return

    if arr[sti][stj] == 1:
        st.append('1')
    else:
        st.append('0')


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
st = []
divide(0, 0, n)
