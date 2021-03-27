def solution(s, n):
    s = list(s)
    for i, a in enumerate(s):
        if (ord(a) > 64) and (ord(a) < 91):
            a = ord(a) + n
            if a > 90:
                over = a - 91
                a = 65 + over
            a = chr(a)
        elif (ord(a) > 96) and (ord(a) < 123):
            a = ord(a) + n
            if a > 122:
                print(a)
                over = a - 123
                a = 97 + over
            a = chr(a)
        s[i] = a

    return "".join(s)
