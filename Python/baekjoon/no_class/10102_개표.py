n = int(input())
result = input()
A = result.count("A")
B = result.count("B")
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")