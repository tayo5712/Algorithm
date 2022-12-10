num = input().split('-')        # - 기준으로 나눔

result = 0
for i in num[0].split("+"):     # 분리된 수식 기준 첫 번째 인덱스만 +
    result += int(i)

for i in num[1:]:               # 나머지 수식앞에는 -가 붙는다.
    for j in i.split('+'):
        result -= int(j)

print(result)
