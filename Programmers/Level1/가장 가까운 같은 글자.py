def solution(s):
    answer = []
    temp = ''

    for i in s:
        if temp.rfind(i) == -1:
            answer.append(-1)
        else:
            result = temp.rfind(i)
            answer.append(len(temp)-result)

        temp+=i

    return answer