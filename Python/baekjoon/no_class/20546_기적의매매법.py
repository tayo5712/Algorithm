cash_j = int(input())
cash_s = cash_j
li = list(map(int, input().split()))
j, s = 0, 0
jj, sj = 0, 0

for i in range(len(li)):
    if li[i] <= cash_j:
        jj += cash_j // li[i]
        cash_j = cash_j % li[i]

j = cash_j + li[-1] * jj

for i in range(3, len(li)):
    if li[i - 3] > li[i - 2] > li[i - 1] > li[i]:
        sj += cash_s // li[i]
        cash_s = cash_s % li[i]

    elif li[i - 3] < li[i - 2] < li[i - 1] < li[i]:
        sj += cash_s // li[i]
        cash_s = cash_s % li[i]

s = cash_s + li[-1] * sj

if j > s:
    print("BNP")
elif j < s:
    print("TIMING")
else:
    print("SAMESAME")
