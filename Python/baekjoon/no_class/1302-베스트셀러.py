N = int(input())
books = {}
for n in range(N):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
ans = sorted(books.items(), key=lambda x:(-x[1],x[0]))
print(ans[0][0])