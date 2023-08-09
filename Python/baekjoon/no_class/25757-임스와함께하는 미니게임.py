game = {"Y": 2, "F": 3, "O": 4}
n, g = input().split()
player = set(input() for _ in range(int(n)))
print(len(player) // (game[g] - 1))