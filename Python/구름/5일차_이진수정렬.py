# https://level.goorm.io/exam/195687/%EC%9D%B4%EC%A7%84%EC%88%98-%EC%A0%95%EB%A0%AC/quiz/1
# 구름 챌린지 5일차

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(key = lambda x : (-bin(x).count("1"), -x))
print(arr[K-1])
