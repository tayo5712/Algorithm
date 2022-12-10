import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    k = int(input())

    apartment = [[0] * (15) for _ in range(15)]

    for i in range(15):
        apartment[0][i] = i     # i층의 1호는 항상 1의 값을 갖는다.
        apartment[i][1] = 1     # 0층의 i호는 i의 값을 지닌다.

    for i in range(1, 15):
        for j in range(2, 15):
            apartment[i][j] = apartment[i][j-1] + apartment[i-1][j] # 점화식

    print(apartment[n][k])
