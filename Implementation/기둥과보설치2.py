def can_construct(pillar_list, bo_list, to_construct, a):
    x, y = to_construct

    if a == 0:  # 기둥
        if y == 0:  # 바닥 위
            return True
        if (x - 1, y) in bo_list or (x, y) in bo_list:  # 보의 한쪽 끝부분 위
            return True
        if (x, y - 1) in pillar_list:  # 다른 기둥 위
            return True
        return False

    else:  # 보
        if (x, y - 1) in pillar_list or (x + 1, y - 1) in pillar_list:  # 한쪽 끝부분이 기둥 위
            return True
        if (x - 1, y) in bo_list and (x + 1, y) in bo_list:  # 양쪽 끝부분이 다른 보와 연결
            return True
        return False


def can_delete(pillar_list, bo_list, to_delete, a):
    if a == 0:  # 기둥
        pillar_list.remove(to_delete)  # 일단 삭제

        # 기둥, 보 전체 확인
        for pillar in pillar_list:
            if not can_construct(pillar_list, bo_list, pillar, 0):
                pillar_list.append(to_delete)
                return False

        for bo in bo_list:
            if not can_construct(pillar_list, bo_list, bo, 1):
                pillar_list.append(to_delete)
                return False

        pillar_list.append(to_delete)  # 복구
        return True

    else:  # 보
        bo_list.remove(to_delete)  # 일단 삭제

        for pillar in pillar_list:
            if not can_construct(pillar_list, bo_list, pillar, 0):  # 안되는거 하나라도 있으면 안됨
                bo_list.append(to_delete)
                return False

        for bo in bo_list:
            if not can_construct(pillar_list, bo_list, bo, 1):
                bo_list.append(to_delete)
                return False

        bo_list.append(to_delete)
        return True


def solution(n, build_frame):
    answer = list()

    pillar_list = list()  # (x1, y1)
    bo_list = list()
    for order in build_frame:
        x, y, a, b = order  # (x, y): 좌표, a: 0(기둥), 1(보), b: 0(삭제), 1(설치)

        if b == 1:  # 설치
            to_construct = (x, y)

            if can_construct(pillar_list, bo_list, to_construct, a):
                if a == 0:  # 기둥
                    pillar_list.append(to_construct)
                else:  # 보
                    bo_list.append(to_construct)

        else:  # 삭제
            to_delete = (x, y)

            if can_delete(pillar_list, bo_list, to_delete, a):
                if a == 0:  # 기둥
                    pillar_list.remove(to_delete)
                else:  # 보
                    bo_list.remove(to_delete)

    # 출력
    for pillar in pillar_list:
        answer.append([pillar[0], pillar[1], 0])

    for bo in bo_list:
        answer.append([bo[0], bo[1], 1])

    answer.sort()
    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
