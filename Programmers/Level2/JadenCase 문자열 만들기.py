def solution(s):

    snew = s[0].capitalize()
    
    for i in range(1, len(s)):
        if s[i] == ' ':
            snew += ' '
        elif s[i-1] != ' ':
            snew += s[i].lower()
        else:
            snew += s[i].capitalize()

    return snew

    # capitalize 문자열에서 맨 첫글자를 대문자로 변환시킨다.
    # title	문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 영단어들의 첫글자를 모두 대문자로 변환시킨다.