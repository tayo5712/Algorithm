l=set()
r=0
for i in range(int(input())):
    n=input()
    if n=='ENTER':
        l=set()
    elif n not in l:
        r+=1
        l.add(n)
print(r)
