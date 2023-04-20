sentence = input()
cnt = 0
for word in sentence:
    if cnt == 0 and word == "U":
        cnt += 1
    elif cnt == 1 and word == "C":
        cnt += 1
    elif cnt == 2 and word == "P":
        cnt += 1
    elif cnt == 3 and word == "C":
        cnt += 1

if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
