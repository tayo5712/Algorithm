import sys

input = sys.stdin.readline
num_balls, num_teams = map(int, input().split())
min_balls = num_teams*(num_teams+1)/2
if min_balls > num_balls:
   print(-1)
else:
   teams = [i for i in range(num_teams-1, -1, -1)]
   num_balls -= min_balls
   while num_balls > 0:
       for i in range(num_teams):
           if num_balls == 0:
               break
           teams[i] += 1
           num_balls -= 1
   print(teams[0]-teams[-1])
