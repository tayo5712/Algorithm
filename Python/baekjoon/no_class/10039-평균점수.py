scores = list(int(input()) for _ in range(5))
total = 0
for score in scores:
    if score < 40:
        total += 40
    else:
        total += score
print(total//5)