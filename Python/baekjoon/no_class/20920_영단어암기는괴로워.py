n, m = map(int, input().split())
word_dict = {}
for _ in range(n):
    word = input()
    if len(word) >= m:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
word_dict = sorted(word_dict.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for key, item in word_dict:
    print(key)