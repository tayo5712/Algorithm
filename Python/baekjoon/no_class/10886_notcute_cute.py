n = int(input())
people = list(int(input()) for _ in range(n))
if people.count(0) > people.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")