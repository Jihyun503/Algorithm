def solution(ingredient):
    temp = []
    answer = 0

    for i in ingredient:
        temp.append(i)
        if len(temp) >= 4:
            if temp[-1] == 1 and temp[-2] == 3 and temp[-3] == 2 and temp[-4] == 1:
                temp.pop()
                temp.pop()
                temp.pop()
                temp.pop()
                answer += 1

    return answer