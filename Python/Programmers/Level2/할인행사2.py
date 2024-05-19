def check(lst):
    possible = True
    for key, value in lst.items():
        if value != 0:
            possible = False
            break
    return possible

def solution(want, number, discount):
    answer = 0
    fruit = dict()
    for i in range(len(want)):
        if want[i] not in fruit:
            fruit[want[i]] = 0
        fruit[want[i]] += number[i]
    
    left = 0
    right = sum(number) - 1
    while right < len(discount):
        if left == 0:
            for i in range(sum(number)):
                if discount[i] in fruit:
                    fruit[discount[i]] -= 1
        else:
            if discount[left - 1] in fruit:
                fruit[discount[left - 1]] += 1
            if discount[right] in fruit:
                fruit[discount[right]] -= 1
        if check(fruit):
            print(left)
            answer += 1
        left += 1
        right += 1
        
    return answer
