N = int(input())
t_shirt = list(map(int, input().split()))
T, P = map(int, input().split())
t_shirt_group = 0
for t in t_shirt:
    t_shirt_group += (t // T) + (1 if t % T else 0)
print(t_shirt_group)
print(f'{sum(t_shirt) // P} {sum(t_shirt) % P}')
