def solution(n):
    answer = 0
    a = format(n, 'b')
    a = a.replace('0', '')

    while 1:
        n+=1
        if len(a.replace('0', '')) == len(format(n, 'b').replace('0', '')):
            answer = n
            break
    return answer