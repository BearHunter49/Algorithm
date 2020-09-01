N = 5  # 데이터 개수
M = 7  # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]  # 전체 데이터

count = 0
interval_sum = 0
end = 0

for start in range(N):

    while interval_sum < M and end < N:  # end 증가시키기
        interval_sum += data[end]
        end += 1

    if interval_sum == M:  # 체크
        count += 1

    interval_sum -= data[start]

print(count)





