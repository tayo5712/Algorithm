import sys
input = sys.stdin.readline

def calculate_line(a, b):
    return (abs(b[0]-a[0])**2 + abs(b[1]-a[1])**2)


n = int(input())

for _ in range(n):
    l = [list(map(int, input().split())) for _ in range(4)]
    l.sort(key=lambda x: (x[0], x[1]))

    answer = [calculate_line(l[0], l[1]),
              calculate_line(l[0], l[2]),
              calculate_line(l[0], l[3]),
              calculate_line(l[1], l[2]),
              calculate_line(l[1], l[3]),
              calculate_line(l[2], l[3]),]
    
    if len(set(answer))==2 and \
        answer.count(max(answer))==2 and \
            answer.count(min(answer))==4: print(1)
    else:
        print(0)
