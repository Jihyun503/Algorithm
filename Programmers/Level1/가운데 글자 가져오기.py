def solution(s):
    answer = ''

    a = len(s)/2

    if(len(s) % 2 == 0):
        answer = s[int(a-1):int(a+1)]
    else :
        answer = s[int(a)]

    return answer