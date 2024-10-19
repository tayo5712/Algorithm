import math

for _ in range(int(input())):
    comp, N, T, L = input().split()
    tt = 0
    if comp == 'O(N)':
        tt = int(N) * int(T)
    elif comp == 'O(N^2)':
        tt = int(N) * int(N) * int(T)
    elif comp == 'O(N^3)':
        tt = int(N) * int(N) * int(N) * int(T)
    elif comp == 'O(2^N)':
        tt = 2 ** int(N) * int(T)
    elif comp == 'O(N!)':
        tt = math.factorial(int(N)) * int(T)
    if tt <= int(L) * (10**8):
        print('May Pass.')
    else:
        print('TLE!')
