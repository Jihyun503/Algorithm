def solution(n, words):
    save = [words[0]]
    for i in range(1, len(words)):
        if words[i] in save:
            return [i%n+1, i//n+1]
        elif words[i][0] != save[-1][-1]:
            return [i%n+1, i//n+1]

        save.append(words[i])

    return [0,0]