N = int(input())

d = [0]*(N+1)
d[0] = 1

for i in range(1, N+1):
    for j in range(i):  
        d[i] += d[j]*d[i-j-1]
    
print(d[N])
