n = int(input())
result = []
cnt = 1

while n != 0:
    name_list = []
    num_list = []
    for i in range(n):
        name_list.append(input())
    for i in range(2*n-1):
        num, label = input().split()
        num = int(num)
        if num in num_list:
            num_list.remove(num)
        else:
            num_list.append(num)
    print(cnt, name_list[num_list.pop()-1])
    cnt += 1
    n = int(input())