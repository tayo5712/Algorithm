for _ in range (int(input())):
    LT, WT, LE, WE = map(int, input().split())
    if LT * WT > LE * WE :
        print("TelecomParisTech")
    elif LT * WT < LE * WE :
        print("Eurecom")
    else :
        print("Tie")