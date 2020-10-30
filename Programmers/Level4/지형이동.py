from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R
group_land = list()
edges = dict()


def do_grouping(land, i, j, now_group, height):
    size = len(land)
    queue = deque()

    queue.append((i, j))
    group_land[i][j] = now_group
    while queue:
        x, y = queue.popleft()
        h = land[x][y]

        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]

            if 0 <= nx < size and 0 <= ny < size:
                nh = land[nx][ny]
                next_group = group_land[nx][ny]
                if next_group != now_group and abs(nh - h) <= height:  # 사다리 노필요
                    queue.append((nx, ny))
                    group_land[nx][ny] = now_group


def find_edges(land):
    global group_land, edges
    n = len(land)

    for i in range(n):
        for j in range(n):
            now_group = group_land[i][j]
            now_height = land[i][j]

            # 오른쪽과 아래만 확인하기
            right = (i, j + 1)
            down = (i + 1, j)
            if right[1] < n:
                next_group = group_land[right[0]][right[1]]
                next_height = land[right[0]][right[1]]
                if now_group != next_group:
                    a, b = min(now_group, next_group), max(now_group, next_group)
                    edges[(a, b)] = min(edges.get((a, b), int(1e9)), abs(next_height - now_height))

            if down[0] < n:
                next_group = group_land[down[0]][down[1]]
                next_height = land[down[0]][down[1]]
                if now_group != next_group:
                    a, b = min(now_group, next_group), max(now_group, next_group)
                    edges[(a, b)] = min(edges.get((a, b), int(1e9)), abs(next_height - now_height))


def find_parent(parent_list, x):
    parent = parent_list[x]

    if parent == x:
        return x
    else:
        parent_list[x] = find_parent(parent_list, parent)  # 경로 압축 기법
        return parent_list[x]


def union_parent(parent_list, a, b):
    a = find_parent(parent_list, a)
    b = find_parent(parent_list, b)

    if a < b:
        parent_list[b] = a
    else:
        parent_list[a] = b


def solution(land, height):
    global group_land, edges
    answer = 0

    n = len(land)
    group_land = [[0] * n for _ in range(n)]
    group = 1

    # Grouping 하기
    for i in range(n):
        for j in range(n):
            if group_land[i][j] == 0:
                do_grouping(land, i, j, group, height)
                group += 1

    # 각 그룹별로 최소 연결 edge 구하기
    find_edges(land)

    # 크루스칼
    parent_list = [i for i in range(group)]
    my_edges = sorted(edges.items(), key=lambda x: x[1])

    for edge in my_edges:
        s, e = edge[0]
        d = edge[1]

        if find_parent(parent_list, s) == find_parent(parent_list, e):  # 싸이클
            continue
        else:
            answer += d
            union_parent(parent_list, s, e)

    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))  # 15
