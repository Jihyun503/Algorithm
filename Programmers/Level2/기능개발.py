def solution(progresses, speeds):
    answer = []
    
    for i, p in enumerate(progresses):
        chk = 0
        while p < 100:
            p += speeds[i]
            chk += 1

    return answer