import heapq


def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    shortest = [INF] * (N + 1)  # 인덱스 0 빼고
    visited = [False] * (N + 1)  # 인덱스 0 빼고
    graph = [[] for _ in range(N + 1)]  # 인덱스 0 빼고

    # edge 정보 기록
    for s, e, d in road:
        graph[s].append((e, d))
        graph[e].append((s, d))

    heap = list()
    shortest[1] = 0  # 1번 시작
    heapq.heappush(heap, (0, 1))  # (distance, node)
    while heap:
        distance, node = heapq.heappop(heap)
        if visited[node]:
            continue

        visited[node] = True

        for e, d in graph[node]:
            origin_distance = shortest[e]
            new_distance = distance + d
            if new_distance < origin_distance:
                shortest[e] = new_distance
                heapq.heappush(heap, (new_distance, e))

    for i in range(1, N + 1):
        if shortest[i] <= K:
            answer += 1

    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))  # 4
