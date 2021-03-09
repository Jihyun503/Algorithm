def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            num = arr1[i][j] + arr2[i][j]
            answer[i].append(num)
    return answer