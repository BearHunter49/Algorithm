import copy


# 리스트에서 값 빼기
def delete_list(weak, fixed):
    new_weak = list()
    for point in weak:
        if point not in fixed:
            new_weak.append(point)

    return new_weak


# 범위 내 수리 가능 지점 찾기
def search(weak, point, n):
    result = list()
    for p in weak:
        if point <= p <= n:
            result.append(p)

    return result


# 최대 수리 가능한 포인트 찾기
def fix(n, distance, weak):
    result_points = list()
    diff = 0

    # 시계 방향
    for point in weak:  # 시작 지점
        fixed_points = list()
        cover = point + distance
        if cover >= n:
            for p in search(weak, point, n):
                fixed_points.append(p)
            for p in search(weak, 0, cover - n):
                fixed_points.append(p)
        else:
            for p in search(weak, point, cover):
                fixed_points.append(p)

        num = len(fixed_points)
        if num > len(result_points):  # 개수가 더 많고
            if result_points:
                if max(result_points) - min(result_points) > diff:  # 포인트 사이의 거리가 클 때
                    result_points = fixed_points
            else:  # result_points 가 비어있다면
                result_points = fixed_points

    # 반시계 방향
    for point in weak:  # 시작 지점
        fixed_points = list()
        cover = point - distance
        if cover < 0:
            for p in search(weak, 0, point):
                fixed_points.append(p)
            for p in search(weak, n + cover, n):
                fixed_points.append(p)
        else:
            for p in search(weak, cover, point):
                fixed_points.append(p)

        num = len(fixed_points)
        if num > len(result_points):  # 개수가 더 많고
            if result_points:
                if max(result_points) - min(result_points) > diff:  # 포인트 사이의 거리가 클 때
                    result_points = fixed_points
            else:  # result_points 가 비어있다면
                result_points = fixed_points

    return result_points


# 현재 인원으로 해결 가능한지 확인
def possible(n, temp_dist, weak):

    for i in range(len(temp_dist)):  # 한 명씩 최대 수리 가능한 포인트들 찾기
        fixed = fix(n, temp_dist[len(temp_dist) - 1 - i], weak)  # 뒤에서 부터(오름차순이라)
        weak = delete_list(weak, fixed)

        if not weak:  # 다 고쳤으면
            return True

    return False


def solution(n, weak, dist):
    answer = -1
    for i in range(len(dist)):  # 인원 바꿔가면서
        temp_dist = dist[i:]

        if possible(n, temp_dist, weak) == True:  # 현재 인원으로 해결 가능
            answer = len(temp_dist)
        else:  # 불가능하면 멈추기
            break

    return answer



print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))


# 못품



