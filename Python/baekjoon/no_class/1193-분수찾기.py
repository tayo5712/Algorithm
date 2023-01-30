x = int(input())
i, num = 0, 0
while x > num:
    i += 1
    num += i

# x가 몇 번째 대각선에 위치하는지 확인 -> while문 탈출하면 x가 몇 번째 대각선에 있는지 i에 저장
# i가 홀수인지 짝수인지 확인해서 분자 분모에 각 값을 대입, num-x로 i번째 대각선의 어느 위치에 있는지 알 수 있다.

if i % 2 == 0 :
    a = i - (num - x)
    b = (num - x) + 1
else:
    a = (num - x) + 1
    b = i - (num - x)

print(f'{a}/{b}')



