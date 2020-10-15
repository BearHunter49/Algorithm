def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[0])  # 시작 지점으로 오름차순 정렬
    last_camera = -30000
    for s, e in routes:
        if s <= last_camera and e <= last_camera:
            last_camera = e

        else:
            answer += 1
            last_camera = e

    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))  # 2

