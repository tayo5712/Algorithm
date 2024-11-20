n,m = map(int, input().split())
 
arr = []
 
for _ in range(n): 
    cardNum = sorted(list(map(int, input().split())), reverse=True)
    arr.append(cardNum)
 
card = n * [0]
 
for i in range(m):
    maxNum = arr[0][i]
    
    for j in range(n):
        maxNum = max(maxNum, arr[j][i])
    
    for j in range(n):
        if arr[j][i] == maxNum:
            card[j] += 1
 
result = []
 
for i in range(len(card)):
    if max(card) == card[i]:
        result.append(i+1)
    
print(*result)
