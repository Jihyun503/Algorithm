def solution(s):
    answer = [0]*2

    while s!='1':
        answer[1]+=s.count('0')
        s = format(len(s.replace('0','')), 'b')
        answer[0]+=1

    return answer