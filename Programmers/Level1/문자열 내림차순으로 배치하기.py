def solution(s):
    a = []
    for i in range(len(s)):
        a.append(s[i])

    a.sort(reverse=True)
    a = "".join(a)

    return a
    