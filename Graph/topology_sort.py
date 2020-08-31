from collections import deque

V, E = map(int, input().split())
indegree_list = [0] * (V + 1)  # 진입 차수 리스트, 인덱스 0 빼고
edge_list = [[] for _ in range(V + 1)]  # 간선 길이 리스트, 인덱스 0 빼고

# 입력
for _ in range(E):
    s, e = map(int, input().split())
    edge_list[s].append(e)  # 간선 정보
    indegree_list[e] += 1  # 진입 차수 증가

result = list()
queue = deque()

# 초기값
for i in range(1, V + 1):
    if indegree_list[i] == 0:
        queue.append(i)

# 위상 정렬
while queue:
    node = queue.popleft()
    result.append(node)

    for edge in edge_list[node]:
        indegree_list[edge] -= 1
        if indegree_list[edge] == 0:
            queue.append(edge)

# 출력
print(result)

# O(V + E) - 처음에 진입 차수 0인 놈 찾는데 O(V), 큐를 돌며 모든 간선 확인 O(E) 따라서 O(V + E)




