import sys

input = sys.stdin.readline

answer = 0
for _ in range(5):
    question = input().rstrip()
    hour = int(question[6:8]) - int(question[0:2])
    minute = int(question[9:11]) - int(question[3:5])
    answer += hour * 60 + minute

print(answer)
