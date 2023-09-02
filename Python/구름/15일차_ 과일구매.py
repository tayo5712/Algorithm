# https://level.goorm.io/exam/195697/%EA%B3%BC%EC%9D%BC-%EA%B5%AC%EB%A7%A4/quiz/1
# 구름 챌린지 15일차

N, K = map(int, input().split())
fruits = [list(map(int, input().split())) for _ in range(N)]
fruits.sort(key=lambda x: -(x[1] // x[0]))
answer = 0
price = 0
for fruit in fruits:
    if price + fruit[0] <= K:
        price += fruit[0]
        answer += fruit[1]
    else:
        answer += (fruit[1] // fruit[0]) * (K - price)
        break
print(answer)
