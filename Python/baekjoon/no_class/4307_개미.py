import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    stick_len, ant_count = map(int, input().split())
    min_time = []
    max_time = []
    for _ in range(ant_count):
        loc = int(input())
        min_time.append(min(loc, stick_len - loc))
        max_time.append(max(loc, stick_len - loc))
    print(max(min_time), max(max_time))
