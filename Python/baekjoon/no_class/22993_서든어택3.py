import sys
input = sys.stdin.readline
input()
c, *li = map(int, input().split())
li.sort()
for a in li:
    if c <= a:
        print('No')
        exit()
    c += a
print('Yes')
