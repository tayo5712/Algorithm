money = 0
while True:
    n = int(input())
    if n == -1:
        print(money)
        break
    else:
        money += n
