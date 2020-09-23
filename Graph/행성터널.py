# 입력
N = int(input())  # 행성 개수

x_list = list()  # (노드번호, x)
y_list = list()  # (노드번호, y)
z_list = list()  # (노드번호, z)

for i in range(N):
    x, y, z = map(int, input().split())
    x_list.append((i, x))
    y_list.append((i, y))
    z_list.append((i, z))


edges = list()  # 간선 정보 (출발, 도착, 거리)

# 각 좌표로 정렬
x_list.sort(key=lambda x: x[1])
y_list.sort(key=lambda x: x[1])
z_list.sort(key=lambda x: x[1])

# 간선 저장
for i in range(N - 1):
    node1, x1 = x_list[i]
    node2, x2 = x_list[i + 1]
    d = abs(x1 - x2)
    edges.append((node1, node2, d))

    node1, y1 = y_list[i]
    node2, y2 = y_list[i + 1]
    d = abs(y1 - y2)
    edges.append((node1, node2, d))

    node1, z1 = z_list[i]
    node2, z2 = z_list[i + 1]
    d = abs(z1 - z2)
    edges.append((node1, node2, d))


# Union-Find
def union_parent(parents, a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)

    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def find_parent(parents, x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_parent(parents[x])  # 경로압축
        return parents[x]


# 크루스칼
parent_list = [i for i in range(N)]  # 각 집 노드의 부모
edges.sort(key=lambda x: x[2])

total = 0
for s, e, d in edges:
    if find_parent(parent_list, s) == find_parent(parent_list, e):  # 싸이클
        continue
    else:
        union_parent(parent_list, s, e)
        total += d

print(total)


