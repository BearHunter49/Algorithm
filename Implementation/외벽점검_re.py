from itertools import permutations


def solution(n, weak, dist):
    answer = 1000

    weak_num = len(weak)  # 취약점 개수
    people_num = len(dist)  # 사람 명수

    # 취약점 배열을 2배로 늘려 시계, 반시계 한번에 보기
    for i in range(weak_num):
        weak.append(weak[i] + n)

    possibles = list(permutations(dist, people_num))  # 모든 가능한 사람 순서
    for i in range(weak_num):  # 출발점

        for possible in possibles:  # 모든 가능성
            next_index = i
            checked = 0  # 고친 취약점 개수
            count = 1  # 사람 수

            for distance in possible:  # 사람 투입

                until = weak[next_index] + distance  # 갈 수 있는 최대 거리

                for index in range(next_index, next_index + weak_num):  # 어디까지 갔나 체크
                    if until >= weak[index]:
                        checked += 1
                        if checked == weak_num:  # 다 고쳤을 경우
                            break
                        continue
                    else:  # 못 간 경우 발견
                        count += 1  # 사람 더 투입
                        next_index = index  # 못 간 지점부터 시작
                        break

                if checked == weak_num:  # 다 고쳤을 경우
                    answer = min(answer, count)
                    break

    if answer == 1000:
        answer = -1
    return answer


print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# 순열, 조합 list 로 안바꿀 시 for 문에서 원소를 소모해버림






