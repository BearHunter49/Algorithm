N = 5  # 리스트 크기
data = [10, 20, 30, 40, 50]  # 데이터

# ---------Self----------
# prefix_sum = [0] * (N + 1)  # 인덱스 0은 빼기
#
# for i in range(1, N + 1):
#     prefix_sum[i] = prefix_sum[i - 1] + data[i - 1]

# -------원본---------
sum_value = 0
prefix_sum = [0]  # 인덱스 0은 빼기

for num in data:
    sum_value += num
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])

# O(N + M) - N은 데이터 크기, M은 쿼리 개수


