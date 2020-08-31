from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]  # 간선 리스트, 인덱스 0 빼고
indegree = [[0, 0] for _ in range(N + 1)]  # (진입 차수, 넘겨받은 최대 수강 시간)
course_time = [0] * (N + 1)

# 입력
for i in range(1, N + 1):
    course_input = list(map(int, input().split()))  # 강의 시간, 선수 과목...., -1

    course_time[i] = course_input[0]  # 강의 시간 저장
    prerequisite = course_input[1:-1]  # 선수 과목 리스트

    for course in prerequisite:
        graph[course].append(i)  # 선수과목 간선 추가
        indegree[i][0] += 1  # 진입 차수 증가

queue = deque()
result = [0] * (N + 1)  # 결과값. 누적 수강 시간

# 초기값
for i in range(1, N + 1):
    if indegree[i][0] == 0:
        queue.append(i)

# 위상 정렬
while queue:
    now = queue.popleft()
    result[now] = indegree[now][1] + course_time[now]  # 현재까지 걸린 최대 시간 + 현재 강의 수강 시간

    for destination in graph[now]:  # 연결된 간선 없애기
        indegree[destination][0] -= 1
        indegree[destination][1] = max(indegree[destination][1], result[now])  # 더 큰 시간을 넘겨주기

        if indegree[destination][0] == 0:  # 0 되면 큐에 넣기
            queue.append(destination)

# 출력
for i in range(1, N + 1):
    print(result[i])






