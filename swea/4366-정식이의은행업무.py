import sys

sys.stdin = open("input_4366.txt", "r")

def cal():
    bi_set = set()
    tri_set = set()

    for i in range(len_bi):
        bi_list = list(binary)
        bi_list[i] = str((int(binary[i]) + 1) % 2)
        bi_set.add(int(''.join(bi_list), 2))

    for j in range(len_tri):
        tri_list = list(trinary)
        for k in range(1, 3):
            tri_list[j] = str((int(trinary[j]) + k) % 3)
            tri_set.add(int(''.join(tri_list), 3))

    answer = bi_set & tri_set
    return answer

for tc in range(1, int(input())+1):
    binary = input()
    trinary = input()
    len_bi = len(binary)
    len_tri = len(trinary)

    print(f'#{tc} {cal()}')


