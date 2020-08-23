N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))

max_num = max(input_list)
input_list.remove(max_num)
sec_max_num = max(input_list)

result = 0

q = M // (K + 1)  # 몫
r = M % (K + 1)  # 나머지

count = q * K + r
result += count * max_num  # 큰 수 더하기
result += (M - count) * sec_max_num

print(result)
