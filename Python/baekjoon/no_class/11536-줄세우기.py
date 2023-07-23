n = int(input())
names = list(input() for _ in range(n))
Inames = sorted(names)
Dnames = sorted(names, reverse=True)
if names == Inames:
    print("INCREASING")
elif names == Dnames:
    print("DECREASING")
else:
    print("NEITHER")

