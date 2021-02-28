def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1) :
        for j in range(i+1,len(phone_book)) :
            if phone_book[i] == phone_book[j][:len(phone_book[i])] :
                return False

    return answer

    # startswith 이란 좋은 함수가 있네..