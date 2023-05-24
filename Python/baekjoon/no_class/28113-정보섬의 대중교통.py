N, A, B = map(int, input().split())
if B-N >= 0 and B < A:
    print("Subway")
elif A < B:
    print("Bus")
else:
    print("Anything")
