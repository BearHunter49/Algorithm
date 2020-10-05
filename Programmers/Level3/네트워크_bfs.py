from collections import deque


def solution(n, computers):
    answer = 0

    checked = [False] * n
    for i in range(n):  # 모든 노드에 대해 탐색
        queue = deque()

        if not checked[i]:  # 아직 탐색 안한 노드
            queue.append(i)
            answer += 1

            while queue:
                node = queue.popleft()
                if checked[node]:
                    continue

                checked[node] = True
                for j in range(n):
                    if node != j and computers[node][j] == 1 and not checked[j]:
                        queue.append(j)

    return answer


print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))  # 1
