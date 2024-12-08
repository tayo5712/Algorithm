n, now = map(int, input().split())
l = list(map(float, input().split()))
bad = 0.0
good = 0.0

if now == 0:
    good = 1.0
else:
    bad = 1.0
    
g_g = l[0]
g_b = l[1]
b_g = l[2]
b_b = l[3]

for i in range(n):
    prev_good = good
    good = good * g_g + bad * b_g
    bad = prev_good * g_b + bad * b_b

print(int(good * 1000))
print(int(bad * 1000))
