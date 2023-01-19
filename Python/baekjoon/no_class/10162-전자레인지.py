A = 300
B = 60
C = 10
N = int(input())
count_A = N // A
count_B = (N % A) // B
count_C = ((N % A) % B) // C
if ((N % A) % B) % C != 0:
    print(-1)
else:
    print(f"{count_A} {count_B} {count_C}")