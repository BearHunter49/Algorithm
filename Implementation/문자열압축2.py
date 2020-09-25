def solution(s):
    answer = 0
    length = len(s)
    min_result = int(1e9)

    for compress_len in range(1, (length // 2) + 1):
        check_count = (length // compress_len) + 1

        total_length = 0
        pivot = ""
        count = 1
        for i in range(check_count):
            string = s[i * compress_len:(i + 1) * compress_len]

            if pivot == string:
                count += 1
            else:
                total_length += len(string)
                if count != 1:
                    total_length += len(str(count))

                # 초기화
                pivot = string
                count = 1

        # 마지막 숫자 길이
        if count != 1:
            total_length += len(str(count))

        if total_length < min_result:
            min_result = total_length

    answer = min_result

    return answer


print(solution("ababcdcdababcdcd"))













