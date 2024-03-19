monkey, dog = map(int, input().split())
remaining = dog - monkey
if remaining == 0:
    print(0)
elif remaining == 1:
    print(1)
elif remaining == 2:
    print(2)
else:
    for i in range(1, 100000000):
        if i * (i + 1) < remaining <= i * (i + 1) + (i + 1):
            print(i * 2 + 1)
            break
        if i * (i + 1) + (i + 1) < remaining <= (i + 1) * (i + 2):
            print(i * 2 + 2)
            break
