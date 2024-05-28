from itertools import product
alpha = ['A', 'E', 'I', 'O', 'U']
words = []
for i in range(1, 6):
    for per in product(alpha, repeat=i):
        words.append(''.join(per))
words = sorted(words)

def solution(word):
    global words
    answer = words.index(word) + 1
    return answer
