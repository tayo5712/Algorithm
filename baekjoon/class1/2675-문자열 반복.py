for _ in range(int(input())):
    n, words = input().split()
    n = int(n)
    for word in words:
        print(word * n, end='')
    print()

