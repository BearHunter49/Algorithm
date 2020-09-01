from itertools import permutations, combinations

data = [1, 2, 3]

# 순열
for x in permutations(data, 2):
    print(x)

print()
# 조합
for x in combinations(data, 2):
    print(x)
print()

print(list(combinations(data, 2)))

