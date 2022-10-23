a = list(range(1, 9))
b = list(range(8, 0, -1))
question = list(map(int, input().split()))
if question == a:
    print('ascending')
elif question == b:
    print('descending')
else:
    print('mixed')
