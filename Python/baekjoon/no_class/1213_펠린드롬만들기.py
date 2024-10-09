from collections import Counter

def make(words, words_count):
    odd_alphabet_count = 0
    odd_alphabet = ''
    for alphabet in words_count:
        if words_count[alphabet] % 2 == 1:
            odd_alphabet_count += 1
            odd_alphabet += alphabet
        if odd_alphabet_count > 1:
            return ("I'm Sorry Hansoo")
    answer = ''
    for i in range(0, len(words), 2):
        if words_count[words[i]] % 2 == 1:
            words_count[words[i]] -= 1
        else:
            answer += words[i]

    tmp = answer[::-1]
    answer += odd_alphabet
    answer += tmp
    return answer


words = sorted(list(input()))
words_count = Counter(words)

print(make(words, words_count))
