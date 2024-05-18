import sys
import itertools
input = sys.stdin.readline
n = int(input().rstrip())
k = int(input().rstrip())
cards = [input().rstrip() for _ in range(n)]
print(len(set("".join(i) for i in itertools.permutations(cards, k))))
