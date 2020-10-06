from collections import deque


def solution(priorities, location):
    answer = 0

    queue = deque()
    prior_counting = [0] * 10  # 중요도 1 ~ 9 (0 제외)

    for i, priority in enumerate(priorities):
        queue.append((priority, i))  # (중요도, index)
        prior_counting[priority] += 1

    printed = 0
    while queue:
        prior, index = queue.popleft()

        not_prior = 0
        for i in range(prior + 1, 10):
            if prior_counting[i] > 0:
                not_prior = 1
                break

        if not_prior == 1:  # 우선순위 더 높은 문서가 존재
            queue.append((prior, index))
        else:  # 현재 우선순위 가장 높음
            printed += 1  # 인쇄
            prior_counting[prior] -= 1
            if index == location:  # 원하던 문서
                answer = printed
                break

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))  # 1
