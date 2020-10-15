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

    for i in range(len(routes)):
        routes[i].append(abs(routes[i][0] - routes[i][1]))

    routes.sort(key=lambda x: x[2])  # 거리로 오름차순 정렬

    camera_section = list()
    for s, e, d in routes:
        is_overlap = False
        for i in range(len(camera_section)):
            if check_overlap([s, e], camera_section[i]):  # 겹침
                is_overlap = True
                camera_section[i] = get_overlapped([s, e], camera_section[i])
                break

        if not is_overlap:  # 겹치는 포인트 없음
            camera_section.append([s, e])
            answer += 1

    return answer


print(solution([[0, 0], [0, 0], [2, 2]]))  # 2

# 틀림
