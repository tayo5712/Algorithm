color_type = int(input())
color_num = list(map(int, input().split()))
color_sum = sum(color_num)
k = int(input())

mulV = [1] * len(color_num)
for i in range(len(color_num)):
    for j in range(k):
        mulV[i] *= (color_num[i]-j)/(color_sum-j)

print(sum(mulV))