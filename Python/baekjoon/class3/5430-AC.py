import sys
input = sys.stdin.readline
from collections import deque

def play(arr):
    r = 0
    if n == 0:
        arr = deque()

    for order in orders:
        if order == 'R':
            r += 1
        elif order == 'D':
            if len(arr) == 0:
                return print('error')
            else:
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if r % 2:
        arr.reverse()
    return print("["+",".join(arr)+"]")

for _ in range(int(input())):
    orders = input()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    play(arr)


