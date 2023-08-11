def solution(sizes):
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
    maxW = 0;
    maxH = 0;
    for size in sizes:
        maxW = max(maxW, size[0])
        maxH = max(maxH, size[1])
    return maxW * maxH