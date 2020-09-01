import math

n = 30
prime_list = [True] * (n + 1)  # 인덱스 0 빼고

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    if prime_list[i] == True:  # 소수이면

        for j in range(i * 2, n + 1, i):  # i를 제외한 i의 배수 지우기
            prime_list[j] = False

# 출력
for i in range(2, n + 1):
    if prime_list[i] == True:
        print(i, end=' ')


