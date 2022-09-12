n = int(input())
result = 1
for i in range(2, n+1):
    result *= i

out = str(result)
cnt = 0
for j in range(len(out)-1, -1, -1):
    if out[j] == '0':
        cnt += 1
    else:
        break

print(cnt)