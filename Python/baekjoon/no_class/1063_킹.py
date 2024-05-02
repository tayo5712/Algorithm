king, stone, n = input().split()
king = [ord(king[0]) - ord('A') + 1, int(king[1])]
stone = [ord(stone[0]) - ord('A') + 1, int(stone[1])]

move_types = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

for _ in range(int(n)):
    idx = move_types.index(input())
    next_king = [king[0] + dx[idx], king[1] + dy[idx]]
    next_stone = [stone[0] + dx[idx], stone[1] + dy[idx]]

    if 1 <= next_king[0] <= 8 and 1 <= next_king[1] <= 8:
        if next_king == stone:
            if 1 <= next_stone[0] <= 8 and 1 <= next_stone[1] <= 8:
                king = next_king
                stone = next_stone
        else:
            king = next_king

print(chr(king[0] + ord("A") - 1) + str(king[1]))
print(chr(stone[0] + ord("A") - 1) + str(stone[1]))
