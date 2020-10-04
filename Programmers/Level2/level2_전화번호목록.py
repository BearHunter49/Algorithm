def solution(phone_book):
    answer = True

    length = len(phone_book)
    phone_book.sort(key=lambda x: len(x))

    for i in range(length):
        pivot = phone_book[i]

        for j in range(i + 1, length):
            if phone_book[j].startswith(pivot):
                return False

    return answer


print(solution(["124","123","1255","567","13"]))
