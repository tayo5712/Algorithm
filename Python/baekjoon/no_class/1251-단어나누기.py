words = list(input())
result = "z" * 51
for i in range(len(words)-1):
    for j in range(i, len(words)):
        a = words[0:i][::-1]
        b = words[i:j][::-1]
        c = words[j:][::-1]
        if len(a) >= 1 and len(b) >= 1 and len(c) >= 1:
            abc = ''.join(a+b+c)
            if abc < result:
                result = abc
print(result)
