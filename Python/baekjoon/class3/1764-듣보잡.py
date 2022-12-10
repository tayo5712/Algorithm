n, m = map(int, input().split())
lst = {}
for _ in range(n):
    name = input()
    lst[name] = 1           # 듣도 못한 사람 이름을 딕셔너리에 넣는다.
result = []
cnt = 0
for _ in range(m):
    name = input()          # 보도 못한 사람 이름이 딕셔너리에 있으면 그 이름을 리스트에 담아준다.
    if name in lst:
        result.append(name)
        cnt += 1            # 인원 수 체크

result.sort()               # 사전 순 정렬
print(cnt)
for i in result:            # 듣보 보도 못한 사람 출력
    print(i)

