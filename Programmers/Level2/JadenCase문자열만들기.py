def solution(s):
    answer = ""
    is_first = 1
    for c in s:
        if c == " ":
            answer += c
            is_first = 1
        else:
            if is_first == 1:
                answer += c.upper()
                is_first = 0
            else:
                answer += c.lower()

    return answer

print(solution(" A  Sdf Fft "))
