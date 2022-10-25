def solution(X, Y):
    x = []
    y = []
    answer = ''

    for i in range(0, 10):
        x.append(X.count(str(i)))
        y.append(Y.count(str(i)))

    for i in range(9, -1, -1):
        if x[i] and y[i]:
            if len(answer) == 0 and i == 0:
                return "0"
            for _ in range(min(x[i],y[i])): 
                answer+=str(i)

    if len(answer) == 0:
        return "-1"

    return answer