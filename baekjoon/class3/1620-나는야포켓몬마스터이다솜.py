import sys
input = sys.stdin.readline
n, m = map(int, input().split())
book_list = []
book_dict = {}
for i in range(n):
    pm = input().rstrip()
    book_list.append(pm)
    book_dict[pm] = i+1

for _ in range(m):
    p = input().rstrip()
    if p.isnumeric():
        print(book_list[int(p)-1])
    else:
        print(book_dict[p])
