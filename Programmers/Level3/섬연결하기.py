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


def solution(n, costs):
    answer = 0

    # 크루스칼
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        s, e, d = cost

        if find_parent(parents, s) != find_parent(parents, e):
            union_parent(parents, s, e)
            answer += d

    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))  # 4

