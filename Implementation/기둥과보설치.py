# 현재 구조물이 정상인지 확인
def possible(answer):
    for frame in answer:
        x, y, a = frame

        if a == 0:  # 기둥
            # 바닥 위에 있거나, 보의 한쪽 끝부분 위, 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:  # 불가능
                return False

        else:  # 보
            # 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    answer = list()

    for frame in build_frame:
        # x, y: 좌표, a: (0: 기둥, 1: 보), b: (0: 삭제, 1:설치)
        x, y, a, b = frame

        if b == 1:  # 설치
            # 설치 할 때는 벽 넘어가는지 확인
            if a == 0 and y == n:  # 기둥
                continue
            elif a == 1 and x == n:  # 보
                continue
            else:
                answer.append([x, y, a])
                if possible(answer) == False:  # 설치 안되면
                    answer.remove([x, y, a])  # 다시 제거

        else:  # 삭제
            answer.remove([x, y, a])
            if possible(answer) == False:  # 삭제 안되면
                answer.append([x, y, a])  # 다시 추가

    answer.sort()
    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))






