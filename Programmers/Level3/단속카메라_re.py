def check_overlap(section1, section2):
    if section1[0] <= section2[1] and section2[0] <= section1[1]:
        return True
    return False


def get_overlapped(section1, section2):
    if section1[0] >= section2[0] and section1[1] >= section2[1]:
        return [section1[0], section2[1]]
    elif section1[0] <= section2[0] and section1[1] <= section2[1]:
        return [section2[0], section1[1]]
    elif section1[0] >= section2[0] and section1[1] <= section2[1]:
        return section1
    else:
        return section2


def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[0])  # 시작 지점으로 오름차순 정렬

    intersection = [routes[0][0], routes[0][1]]  # 맨 처음 기준
    answer += 1
    for i in range(1, len(routes)):
        if check_overlap(routes[i], intersection):
            intersection = get_overlapped(routes[i], intersection)
        else:
            intersection = routes[i]
            answer += 1

    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))  # 2

