def solution(progresses, speeds):
    answer = []
    for i, p in enumerate(progresses):
        chk = 0
        while p < 100:
            p += speeds[i]
            chk += 1

        if i == 0:
            temp = 1
            min = chk
        else:
            if min >= chk:
                temp += 1
            else:
                answer.append(temp)
                temp = 1
                min = chk

            if i+1 == len(progresses) :
                answer.append(temp)

    return answer