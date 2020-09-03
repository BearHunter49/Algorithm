N, M = map(int, input().split())  # N: 볼링공 개수, M: 공의 최대 무게
balls = list(map(int, input().split()))  # 볼링공 무개 리스트, 인덱스가 번호

balls.sort()  # 오름차순 정렬

result = 0
for i in range(N):
    now_ball = balls[i]

    for j in range(i + 1, N):
        if balls[j] != now_ball:  # 같은 무게면
            result += (N - j)  # 그 뒤는 다 가능한 조합임
            break

print(result)








