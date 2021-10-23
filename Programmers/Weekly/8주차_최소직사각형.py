def solution(sizes):
    maxsize = []
    minsize = []

    for size in sizes:
        maxsize.append(max(size))
        minsize.append(min(size))

    return max(maxsize) * max(minsize)