import itertools

def solution(k, dungeons):

    for i in range(len(dungeons), 0, -1):

        for per in itertools.permutations(dungeons, i):
            now = k
            flag = True 
            for dungeon in per:
                if now >= dungeon[0]:
                    now -= dungeon[1]
                else:
                    flag = False
                    break
            if flag:
                return i
