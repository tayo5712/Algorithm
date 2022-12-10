n = int(input())
m = int(input())
s = input()
check = 0
answer = 0
i = 0
while i < m-2:
    if s[i:i+3] == 'IOI':
        check += 1
        i += 2
        if check == n:
            answer += 1
            check -= 1
    else:
        i += 1
        check = 0

print(answer)