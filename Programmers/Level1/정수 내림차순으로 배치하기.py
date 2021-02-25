def solution(n):
    answer = 0

    n = list(str(n))
    n = list(map(int, n))

    n.sort(reverse=True)

    n1 = list(map(str, n))
    answer = "".join(n1)

    return int(answer)