N = int(input())  # 삼각형 크기
triangle_list = list()

for _ in range(N):
    triangle_list.append(list(map(int, input().split())))

for i in range(1, N):  # 2번째 줄 부터 시작
    for j in range(i + 1):
        left_up = 0
        right_up = 0

        # 왼쪽 위
        if j == 0:
            left_up = 0
        else:
            left_up = triangle_list[i - 1][j - 1]

        # 오른쪽 위
        if j == i:
            right_up = 0
        else:
            right_up = triangle_list[i - 1][j]

        triangle_list[i][j] += max(left_up, right_up)

# 마지막 줄 중 최대값 출력
print(max(triangle_list[-1]))













