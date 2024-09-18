while True:
    n = int(input())
    if n == 0:
        break
    else:
        students = list(input().split() for _ in range(n))
        students = sorted(students, key = lambda x : -float(x[1]))
        maxV = 0
        for student in students:
            if float(student[1]) >= maxV:
                maxV = float(student[1])
                print(student[0], end = ' ')
        print()
