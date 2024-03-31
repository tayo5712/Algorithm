s = input()
a = s.count('a')

s += s[:a-1]
minV = 1001

for i in range(len(s) - (a - 1)):
    minV = min(minV, s[i:i+a].count('b'))
print(minV)
