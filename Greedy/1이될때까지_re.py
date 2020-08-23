N, K = map(int, input().split())

count = 0
while N != 1:
    q = N // K
    r = N % K

    # 1번
    N -= r
    count += r

    # 2번
    N = q
    count += 1

print(count)
