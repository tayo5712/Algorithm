from collections import Counter

a = [-3, -3, 2, 53, 23, 21, 11, 11, 23, 44, 14, -3]
cnt_a = Counter(a).most_common(2)
print(cnt_a)