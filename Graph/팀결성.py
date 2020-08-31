N, M = map(int, input().split())
team_list = [i for i in range(N + 1)]  # 인덱스 0 ~ N 까지, 자기 자신이 팀


# 입력
def union_team(a, b):
    a_team = find_team(a)
    b_team = find_team(b)
    if a_team < b_team:
        team_list[b_team] = a_team
    else:
        team_list[a_team] = b_team


def find_team(x):
    team = team_list[x]
    if x == team:
        return x
    else:
        team_list[x] = find_team(team)  # 경로 압축
        return team_list[x]


result = list()  # 확인 리스트
for _ in range(M):
    num, a, b = map(int, input().split())

    if num == 0:  # 팀 합치기
        union_team(a, b)

    else:  # 같은 팀 여부 확인
        if find_team(a) == find_team(b):  # 같은 팀
            result.append("YES")
        else:
            result.append("NO")

for answer in result:
    print(answer)





