import sys
n = int(sys.stdin.readline())

nazzi = [0] * (n + 1) 
nazzi[1] = 1 
if n > 1:
    nazzi[2] = 2 

for i in range(3, n+1):
    nazzi[i] = (nazzi[i - 1] + nazzi[i - 2]) % 15746  

print(nazzi[n])
