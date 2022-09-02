from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
num2 = sorted(num)
num_dict = {}
cnt_num = Counter(num2).most_common(2)

print(round(sum(num)/n))
print(num2[n//2])
if n == 1:
    print(num[0])
else:
    if cnt_num[0][1] == cnt_num[1][1]:
        print(cnt_num[1][0])
    else:
        print(cnt_num[0][0])
print(max(num)-min(num))