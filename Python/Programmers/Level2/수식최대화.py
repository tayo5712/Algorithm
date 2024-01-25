from itertools import permutations

def solution(expression):
    answer = 0
    numbers = []
    operators = []
    number_length = 0
    answer = 0
    for i in range(len(expression)):
        if expression[i].isdigit():
            number_length += 1

            if i + 1 == len(expression) or not expression[i+1].isdigit():
                numbers.append(int(expression[i - number_length + 1:i + 1]))
                number_length = 0
        else:
            operators.append(expression[i])
            number_length = 0

    for per in permutations(["*", "-", "+"], 3):
        opers = operators.copy()
        nums = numbers.copy()
        for op in per:
            while op in opers:
                index = opers.index(op)
                if op == "+":
                    v = nums[index] + nums[index + 1]
                elif op == "-":
                    v = nums[index] - nums[index + 1]
                else:
                    v = nums[index] * nums[index + 1]
                nums[index] = v
                nums.pop(index + 1)
                opers.pop(index)

        answer = max(answer, abs(nums[0]))
    return answer
