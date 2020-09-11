from bisect import bisect_left, bisect_right

G = int(input())  # 탑승구 수
P = int(input())  # 비행기 수

parent_list = [i for i in range(G + 1)]  # 인덱스 1부터 시작


def find_parent(x):
    if parent_list[x] == x:
        return x
    else:
        parent_list[x] = find_parent(parent_list[x])
        return parent_list[x]


def union_parent(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)

    if a_parent < b_parent:
        parent_list[b_parent] = a_parent
    else:
        parent_list[a_parent] = b_parent


# 입력
flight_list = list()
for _ in range(P):
    flight_list.append(int(input()))

result = 0
for in_flight in flight_list:

    parent = find_parent(in_flight)

    if parent == 0:  # 꽉 참
        break
    else:
        result += 1
        union_parent(parent, parent - 1)

print(result)
















