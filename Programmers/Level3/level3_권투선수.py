def solution(n, results):
    inf = int(1e9)
    edges = [[inf] * (n + 1) for _ in range(n + 1)]  # 인덱스 0 빼고
    for i in range(1, n + 1):
        edges[i][i] = 0

    for win, lose in results:
        edges[lose][win] = 1

    # 플로이드-워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

    # check
    answer = n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if edges[i][j] == inf and edges[j][i] == inf:  # 순위 알 수 없음
                answer -= 1
                break

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
