def solution(s):
    result = int(1e9)  # 최종 결과값 INF
    length = len(s)
    if length == 1:  # 1자리 문자
        return 1

    for i in range(1, (length // 2) + 1):  # 절반 개수까지만 자르기 가능

        # 초기값
        check_string = s[:i]
        total_count = 0
        count = 0
        for j in range(0, length, i):  # i 칸씩 건너뛰기
            now = s[j:j + i]

            if check_string == now:
                count += 1

            else:
                if count != 1:  # 숫자 자리수 + 문자 개수
                    total_count += len(str(count)) + len(check_string)
                else:  # 1개는 숫자 포함 안시키기
                    total_count += len(check_string)

                check_string = now  # check 문자열 변경
                count = 1  # 1로 시작

        # 마지막 처리
        if count != 1:  # 숫자 개수 + 문자 개수
            total_count += len(str(count)) + len(check_string)
        else:  # 1개는 숫자 포함 안시키기
            total_count += len(check_string)

        # 결과값 계산
        if total_count < result:
            result = total_count

    return result


print(solution("aaaa"))



