import sys

input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse = True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse = True)

cnt = 0
if cranes[0] < boxes[0]:
    cnt = -1
else:
    while len(boxes) > 0:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break

        cnt += 1

print(cnt)
