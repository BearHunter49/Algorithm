def find_parent(parents, x):
    if parents[x] == x:
        return x

    parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a_parent = find_parent(parents, a)
    b_parent = find_parent(parents, b)

    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def solution(n, computers):
    parents = [0] * n
    for i in range(n):
        parents[i] = i

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union_parent(parents, i, j)

    networks = set()
    for parent in parents:
        networks.add(find_parent(parents, parent))

    answer = len(networks)
    return answer


print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))  # 1
