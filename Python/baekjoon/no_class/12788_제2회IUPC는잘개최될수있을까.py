n = int(input())
m,k = map(int, input().split())
 
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
 
result = 0
for i in range(n):
 
    if m*k > sum(a):
        print("STRESS")
        break
 
    result += a[i]
    
    if m*k > result:
        continue
    else:
        print(i+1)
        break
