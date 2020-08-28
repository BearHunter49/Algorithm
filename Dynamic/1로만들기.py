X = int(input())
result_set = set()


def make_one(value, count):
    # break 문
    if value == 1:
        result_set.add(count)
        return

    if value % 5 == 0:
        make_one(value // 5, count + 1)
    if value % 3 == 0:
        make_one(value // 3, count + 1)
    if value % 2 == 0:
        make_one(value // 2, count + 1)
    make_one(value - 1, count + 1)


make_one(X, 0)
print(sorted(result_set)[0])

