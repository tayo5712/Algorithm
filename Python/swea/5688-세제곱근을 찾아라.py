import sys
sys.stdin = open("input_5688.txt", "r")

for tc in range(1, int(input())+1):
    n = int(input())**(1/3)
    if 0 <= (round(n)-n) < 0.000000001:
        print(f"#{tc}", end=' ')
        print(round(n))
    else:
        print(f"#{tc}", end=' ')
        print(-1)
