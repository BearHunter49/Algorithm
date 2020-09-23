N, M = map(int, input().split())  # N: 집 개수, M: 도로 개수

edges = []
total_cost = 0  # 총 가로등 비용
for _ in range(M):  # 입력
    s, e, d = map(int, input().split())  # 시작점, 도착점, 거리
    edges.append((s, e, d))
    total_cost += d

parents = [i for i in range(N)]  # 각 집 노드의 부모


def union_parent(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)

    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def find_parent(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_parent(parents[x])  # 경로압축
        return parents[x]


# 크루스칼
edges.sort(key=lambda x: x[2])  # 거리 기준으로 오름차순 정렬
min_total_cost = 0
for s, e, d in edges:
    # 사이클
    if find_parent(s) == find_parent(e):
        continue
    else:
        union_parent(s, e)
        min_total_cost += d

print(total_cost - min_total_cost)

