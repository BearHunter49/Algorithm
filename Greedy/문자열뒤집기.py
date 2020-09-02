S = input()

conseq_list = [0, 0]

pivot = S[0]
for num in S:
    if num != pivot:  # 값이 바뀌면
        conseq_list[int(pivot)] += 1
        pivot = num

conseq_list[int(pivot)] += 1  # 마지막 케이스 추가

print(min(conseq_list[0], conseq_list[1]))






