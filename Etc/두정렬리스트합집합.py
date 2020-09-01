N, M = 3, 4  # 두 리스트 크기
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (N + M)
i, j, k = 0, 0, 0

while True:  # 둘 다 끝날 때 까지
    if (i < N and a[i] < b[j]) or j >= M:  # a가 더 작거나, b 처리가 다 끝났을 때
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

    if i == N and j == M:  # 두 리스트 모두 돌았으면 끝내기
        break

print(result)









