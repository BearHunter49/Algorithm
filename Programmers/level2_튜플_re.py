import re


def solution(s):
    answer = []
    s = s[1:-1]

    splitted = re.findall(r'\{(.*?)\}', s)
    splitted = sorted(splitted, key=lambda x: len(x))  # 길이로 오름차순 정렬

    # 각 문자열을 정수형으로 비교
    for string in splitted:
        num_list = list(map(int, string.split(',')))
        for number in num_list:  # 새로운 숫자 추가
            if number not in answer:
                answer.append(number)
                break

    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))





