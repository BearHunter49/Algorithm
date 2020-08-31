V, E = map(int, input().split())  # 노드 개수, 간선 개수
parent_list = [i for i in range(V + 1)]  # 부모 노드 리스트, 인덱스 0 빼기


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


for _ in range(E):
    s, e = map(int, input().split())
    union_parent(s, e)


# 노드가 속한 집합 출력
print("각 노드가 속한 집합: ", end=' ')
for i in range(1, V + 1):
    print(find_parent(i), end=' ')
print()

# 부모 노드 리스트 출력
print("부모 테이블: ", end=' ')
for i in range(1, V + 1):
    print(parent_list[i], end=' ')


# 경로 압축 안할 시 O(VM) - 부모 찾는데 최대 O(V), union-find 횟수 M
