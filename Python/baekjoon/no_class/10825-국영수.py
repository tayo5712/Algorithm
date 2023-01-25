n=int(input())
a = list(input(). split() for _ in range(n))
a.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0],))

for i in range(n):
    print(a[i][0])