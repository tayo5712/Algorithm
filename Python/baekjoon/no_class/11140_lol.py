import sys
import string

def solve(word):
    if "lol" in word:
        return 0
    elif "lo" in word or "ol" in word or "ll" in word or any("l" + x + "l" in word for x in string.ascii_lowercase):
        return 1
    elif "l" in word or "o" in word:
        return 2
    return 3

input = sys.stdin.readline
t = int(input())
for i in range(t):
    word = input().rstrip()
    print(solve(word))
