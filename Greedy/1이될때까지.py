N, K = map(int, input().split())

count = 0
while N != 1:
    q = N // K
    r = N % K

    if r == 0:  # 2번 될 때
        N = q
    else:  # 1번만 될 때
        N -= 1

    count += 1

    if N == 1:
        break


print(count)
