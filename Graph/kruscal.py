V, E = map(int, input().split())  # 노드 개수, 간선 개수
parent_list = [i for i in range(V + 1)]  # 부모 노드 리스트, 인덱스 0 빼기
edges = []  # 간선 길이 리스트


def find_parent(x):
    parent = parent_list[x]

    if parent == x:
        return x
    else:
        parent_list[x] = find_parent(parent)  # 경로 압축 기법
        return parent_list[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent_list[b] = a
    else:
        parent_list[a] = b


# 입력
for _ in range(E):
    s, e, d = map(int, input().split())
    edges.append((s, e, d))  # 시작점, 도착점, 거리

edges.sort(key=lambda x: x[2])  # 거리로 오름차순 정렬

# 크루스칼
total_distance = 0
for edge in edges:
    s, e, d = edge

    if find_parent(s) == find_parent(e):  # 싸이클
        continue
    else:
        total_distance += d
        union_parent(s, e)

print(total_distance)

# O(ElogE) - 정렬에 드는 비용이 가장 큼
