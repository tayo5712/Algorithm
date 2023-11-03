import sys

input = sys.stdin.readline
ms = {"a": "A", "b": "B", "k": "C",
           "d": "D", "e": "E", "g": "F",
           "h": "G", "i": "H", "l": "I",
           "m": "J", "n": "K",
           "o": "M", "p": "N", "r": "O",
           "s": "P", "t": "Q", "u": "R",
           "w": "S", "y": "T"
           }

def change_ms(word):
    result = word.replace("ng", "L")
    for k, v in ms.items():
        result = result.replace(k, v)
    return result

def solution(arr):
    result = dict()
    for i in arr:
        tmep = change_ms(i)
        result[i] = tmep
    result = sorted(result.items(), key=lambda x: x[1])
    return result

array = []
N = int(input())
for _ in range(N):
    array.append(input().rstrip())
answer = solution(array)
for i in answer:
    print(i[0])
