N, M = map(int, input().split())
edge_list = list()
parent_list = [i for i in range(N + 1)]  # 인덱스 0 제외


def find_parent(x):
    parent = parent_list[x]
    if parent == x:
        return x
    else:
        parent_list[x] = find_parent(parent)
        return parent_list[x]


def union_parent(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if a_parent < b_parent:
        parent_list[b_parent] = a_parent
    else:
        parent_list[a_parent] = b_parent


# 입력
for _ in range(M):
    A, B, C = map(int, input().split())  # 집A, 집B, 유지비
    edge_list.append((A, B, C))

edge_list.sort(key=lambda x: x[2])  # 유지비 오름차순 정렬

# 크루스칼
total_distance = 0
last_distance = 0
for edge in edge_list:
    A, B, C = edge

    if find_parent(A) == find_parent(B):  # 싸이클
        continue
    else:
        total_distance += C
        last_distance = C
        union_parent(A, B)

# 마을 2개로 나누기
print(total_distance - last_distance)




