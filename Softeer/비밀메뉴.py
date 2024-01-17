import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
manual = list(input().split())
control = list(input().split())

if ''.join(manual) in ''.join(control):
    print("secret")
else:
    print("normal")
