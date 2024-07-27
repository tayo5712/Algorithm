prime_number = [True] * 1000
prime_number[0] = False
prime_number[1] = False
li = []
for i in range(2, 1000):
    if prime_number[i]:
        li.append(i)
        for j in range(2*i, 1000, i):
            prime_number[j] = False

def prime_number_sum(x):
    result = []
    for a in range(len(li)):
        for b in range(len(li)):
            for c in range(len(li)):
                if li[a] + li[b] + li[c] == x:
                    result.append([li[a], li[b], li[c]])
    result = sorted(result, key = lambda x : (x[0], x[1], x[2]))
    if len(result) == 0:
        print(0)
    else:
        print(*result[0])

T = int(input())
for _ in range(T):
    K = int(input())
    prime_number_sum(K)
