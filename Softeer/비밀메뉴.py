import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
menu = "".join(input().split())
control = "".join(input().split())
if menu in control:
    print("secret")
else:
    print("normal")