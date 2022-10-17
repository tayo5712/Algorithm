def step1(nums):
    st = []
    word = []

    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    osp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

    for num in nums:
        if num.isalpha():
            word.append(num)
        elif num == ')':
            while st and st[-1] != '(':
                word.append(st.pop())
            st.pop()

        else:
            if not st:
                st.append(num)
            elif osp[num] > isp[st[-1]]:
                st.append(num)
            else:
                while st and isp[st[-1]] >= osp[num]:
                    word.append(st.pop())
                st.append(num)
    while st:
        word.append(st.pop())

    return ''.join(word)

nums = input()
result = step1(nums)
print(result)