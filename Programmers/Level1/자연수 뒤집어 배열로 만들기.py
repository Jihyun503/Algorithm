def solution(n):
    answer = []
    strN = str(n)
    answer = [int(strN[x]) for x in range(len(strN)-1, -1, -1)]
    return answer