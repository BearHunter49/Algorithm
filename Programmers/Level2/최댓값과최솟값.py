def solution(s):
    str_list = list(map(int, s.split()))

    return str(min(str_list)) + " " + str(max(str_list))


print(solution("-1 -2 -3 -4"))



