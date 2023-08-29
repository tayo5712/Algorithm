
def powerset(i, sumV):
    global minV
    if sumV >= b:
        if minV > sumV:
            minV = sumV
        return

    if i == n:
        return

    else:
        powerset(i + 1, sumV + people[i])
        powerset(i + 1, sumV)

T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    people = list(map(int, input().split()))
    visited = [-1] * n
    minV = 2000001
    powerset(0, 0)
    print(f'#{tc} {minV-b}')