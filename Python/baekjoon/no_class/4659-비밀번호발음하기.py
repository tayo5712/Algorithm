
vowels = ["a", "e", "i", "o", "u"]
while (True):
    result = False
    word = input()
    if word == "end":
        exit()
    else:
        for vowel in vowels:
            if vowel in word:
                result = True
                break
        if result:
            for i in range(len(word)):
                if i + 1 <= len(word)-1:
                    if word[i] == word[i+1]:
                        if not (word[i] == "e" or word[i] == "o"):
                            result = False
                            break

                if i + 2 <= len(word)-1:
                    if word[i] in vowels:
                        if word[i+1] in vowels and word[i+2] in vowels:
                            result = False
                            break
                    else:
                        if word[i+1] not in vowels and word[i+2] not in vowels:
                            result = False
                            break
    if result:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')

