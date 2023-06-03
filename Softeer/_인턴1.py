import sys
import itertools
import copy

input = sys.stdin.readline

def cycle(sti, curC):
    global system
    if sign[sti] in curC:
        system.append(curC)
        return

    if visited[sti]:
        return

    curC.append(sign[sti])
    visited[sti] = 1
    cycle(sign[sti]-1, curC)

def cycle2(sti, curC):
    global system2
    if sign2[sti] in curC:
        system2.append(curC)
        return

    if visited2[sti]:
        return

    curC.append(sign2[sti])
    visited2[sti] = 1
    cycle2(sign2[sti]-1, curC)


n = int(input().rstrip())
sign = list(map(int, input().split()))
visited = [0 for _ in range(n)]
system = []
result = 0

for i in range(n):
    if not visited[i]:
        curC = []
        cycle(i, curC)

for s in system:

    if len(s) > 3:
        coms = itertools.combinations(s, 2)
        for com in coms:
            sign2 = copy.deepcopy(sign)
            system2 = []
            visited2 = [0 for _ in range(n)]
            sign2[com[0]-1], sign2[com[1]-1] = sign2[com[1]-1], sign2[com[0]-1]
            for i in range(n):
                if not visited2[i]:
                    curC2 = []
                    cycle2(i, curC2)
            if len(system2) == len(system) + 1:
                result += 1
    elif len(s) > 1:
        result += len(s)

print(result)

# input
# 8
# 8 6 7 4 1 3 2 5
# output
# 9