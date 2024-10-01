n = int(input())
numList = [list(map(int,input().split())) for _ in range(n)]

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a


for list in numList:
    ansList=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            if i!=j:
                ansList.append(gcd(list[i],list[j]))
    print(max(ansList))
