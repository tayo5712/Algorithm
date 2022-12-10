for _ in range(int(input())):
    n = int(input())
    clothes = {}
    for i in range(n):
        cloth, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    result = 1
    for value in clothes.values():
        result *= (value + 1)
    print(result-1)