def count_sheep(n):
    if n == 0:
        return "INSOMNIA"

    seen_digits = set()
    current_number = 0

    while len(seen_digits) < 10:
        current_number += n
        seen_digits.update(str(current_number))

    return current_number

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Case #{i}: {count_sheep(n)}")
