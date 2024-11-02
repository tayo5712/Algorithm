n,w  = map(int,input().split())
cnt = 0
coin = [int(input()) for _ in range(n)]

for i in range(n-1):
	if coin[i] < coin[i+1]:
		if w // coin[i] > 0:
			cnt = w // coin[i]
			w = w % coin[i]
	
	elif coin[i] > coin[i-1]: 
		w += cnt*coin[i]
		cnt = 0
		
if cnt != 0:
	w += cnt*coin[-1]

print(w)
