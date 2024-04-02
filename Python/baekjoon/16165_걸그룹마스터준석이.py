n, m = map(int, input().split())
teams = dict()

for _ in range(n):
    team = input()
    member_num = int(input())
    teams[team] = [input() for _ in range(member_num)]

for _ in range(m):
    name = input()
    if int(input()) == 1:
        for team, members in teams.items():
            if name in members:
                print(team)
    else:
        print('\n'.join(sorted(teams[name])))
