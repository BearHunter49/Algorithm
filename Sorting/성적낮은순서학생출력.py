N = int(input())

students_dict = dict()
for _ in range(N):
    name, score = input().split()
    students_dict[name] = int(score)

result = sorted(students_dict.items(), key=lambda x: x[1])

for student in result:
    print(student[0], end=' ')
