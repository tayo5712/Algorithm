n = int(input())
people = set()
meet_chong = False
for _ in range(n):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong':
        people.add(a)
        people.add(b)
        continue

    if a in people:
        if b in people:
            continue
        else:
            people.add(b)
    elif b in people:
        if a in people:
            continue
        else:
            people.add(a)
print(len(people))

