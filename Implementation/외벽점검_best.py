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
            count = 1  # 투입한 사람 수
            until = weak[i] + possible[count - 1]  # 어디까지 점검 가능한가

            for index in range(i, i + weak_num):
                if until < weak[index]:  # 점검 못 하는 경우
                    count += 1  # 1명 더 투입
                    if count > people_num:  # 인원 다 썼으면
                        break
                    until = weak[index] + possible[count - 1]  # 점검 가능한 거리 갱신

            answer = min(answer, count)
   
    if answer == 1000:
        answer = -1
    return answer


print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# 순열, 조합 list 로 안바꿀 시 for 문에서 원소를 소모해버림




