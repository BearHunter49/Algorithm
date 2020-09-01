import math

M, N = map(int, input().split())

bigger = max(M, N)
smaller = min(M, N)
prime_list = [True] * (bigger + 1)  # 인덱스 0 빼고
prime_list[1] = False  # 1은 소수가 아니다

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(bigger)) + 1):

    if prime_list[i] == True:  # 소수면
        for j in range(i * 2, bigger + 1, i):  # i는 빼고, i의 배수 소수 제외시키기
            prime_list[j] = False

# 출력
for i in range(smaller, bigger + 1):
    if prime_list[i] == True:
        print(i)





