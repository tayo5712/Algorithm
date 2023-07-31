
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Tree = list(map(int, input().split()))
    maxV = max(Tree)
    odd = 0     # 필요한 홀수 날의 개수
    even = 0    # 짝수
    for i in range(N):
        odd += (maxV-Tree[i]) % 2
        even += (maxV-Tree[i]) // 2

    # 짝 수의 개수 만큼의 걸리는 날짜와 홀 수의 개수 만큼의 걸리는 날짜를 비교
    # 홀 수날은 1 0 1 순이므로 홀수의 개수 * 2 - 1 해줘야 걸리는 날이 나온다.
    # 짝수 날과 홀수 날의 쌍을 최대한 비슷하게 맞춰줘야 최소걸리는 날짜가 낭노다.
    result = max(odd * 2 - 1, even * 2)
    while result >= max(odd * 2 - 1, even * 2):
        result = max(odd * 2 - 1, even * 2)
        even -= 1   # 짝수의 개수를 하나 까면 홀수의 개수는 두개 늘어난다.
        odd += 2

    print(f'#{tc} {result}')

