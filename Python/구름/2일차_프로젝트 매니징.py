# https://level.goorm.io/exam/195684/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%A7%A4%EB%8B%88%EC%A7%95/quiz/1
# 구름 챌린지 2일차

n = int(input())
t, m = map(int, input().split())
time = 60 * t + m
for _ in range(n):
	time += int(input())
print((time // 60) % 24, time % 60)