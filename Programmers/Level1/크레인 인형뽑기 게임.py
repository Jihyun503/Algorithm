def solution(board, moves):
    answer = 0
    idx = 0
    chk = [0]
    for move in moves :
        while board[idx][move-1] == 0:
            idx = idx+1
            if idx > len(board)-1 :
                break
                
        if idx > len(board)-1 :
            pass
        else :
            if chk[-1]!=board[idx][move-1]:
                chk.append(board[idx][move-1])
                board[idx][move-1] = 0
            else :
                answer = answer+2
                del chk[-1]
                board[idx][move-1] = 0
        idx = 0

    return answer