N, M = map(int, input().split())  # N: 여행지 수, M: 여행 계획 수

world = list()
for _ in range(N):
    world.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

# 인덱스 0부터 시작으로 바꿔주기
for i in range(len(plan)):
    plan[i] -= 1

# Union-Find
parent_list = [i for i in range(N)]  # 자기 자신을 부모로


def find_parent(x):
    if parent_list[x] == x:  # 자기 자신
        return x
    else:
        parent_list[x] = find_parent(parent_list[x])  # 경로 압축
        return parent_list[x]


def union_parent(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)

    if a_parent < b_parent:
        parent_list[b_parent] = a_parent
    else:
        parent_list[a_parent] = b_parent


# 간선 정보로 부모 합치기
for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            union_parent(i, j)

# 확인하기
parent = find_parent(plan[0])
result = True
for destination in plan:
    if find_parent(destination) != parent:  # 부모 다른 여행지 나오면 실패
        result = False
        break

# 출력
if result == True:
    print("YES")
else:
    print("NO")



