n, m = map(int, input().split())
j = int(input())
l_position = 1
r_position = m
total = 0
for _ in range(j):
    position = int(input())
    if position < l_position:
        total += (l_position - position)
        l_position = position
        r_position = position + (m-1)
    elif position > r_position:
        total += (position - r_position)
        l_position = position - (m-1)
        r_position = position
print(total)
