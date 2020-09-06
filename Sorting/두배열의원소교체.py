N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    min_A = min(A)
    max_B = max(B)
    if min_A < max_B:
        A.remove(min_A)
        A.append(max_B)

        B.remove(max_B)
        B.append(min_A)

print(sum(A))

