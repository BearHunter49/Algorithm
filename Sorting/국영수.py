N = int(input())  # 학생 수

information = list()
for _ in range(N):
    name, kuk, eng, mat = input().split()
    information.append((name, int(kuk), int(eng), int(mat)))

# 쩐다 이 기능
information.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름 출력
for i in range(N):
    print(information[i][0])






