answer = ''
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        answer += str(i) + ' '
if answer == '':
    print('HE GOT AWAY!')
else:
    print(answer)
