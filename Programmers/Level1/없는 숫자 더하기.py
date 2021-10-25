def solution(numbers):
    answer = 0
    numbers = set([1,2,3,4,5,6,7,8,9]) - set(numbers)
    for num in numbers:
        answer+=num
    return answer