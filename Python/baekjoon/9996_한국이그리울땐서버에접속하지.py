n = int(input())
pattern = input().split("*")
length = len(pattern[0]) + len(pattern[1])

for _ in range(n):
    target = input()
    
    if len(target) >= length and target.startswith(pattern[0]) and target.endswith(pattern[1]):
        print("DA")
    else:
        print("NE")
