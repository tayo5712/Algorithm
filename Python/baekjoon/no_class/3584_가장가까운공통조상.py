T = int(input())
for _ in range(T):
    N = int(input())
    parents = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parents[b] = a
    target_a, target_b = map(int, input().split())

    parents_a = [target_a]
    parents_b = [target_b]

    while parents[target_a]:
        parents_a.append(parents[target_a])
        target_a = parents[target_a]

    while parents[target_b]:
        parents_b.append(parents[target_b])
        target_b = parents[target_b]

    idx_a = len(parents_a) - 1
    idx_b = len(parents_b) - 1

    while parents_a[idx_a] == parents_b[idx_b]:
        idx_a -= 1
        idx_b -= 1

    print(parents_a[idx_a + 1])

