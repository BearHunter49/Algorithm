arr = [2 * x - 1 for x in range(1, 11)]
print(arr)


def binary_search(target, start, end):
    # break
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:  # found
        return mid
    elif arr[mid] < target:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid - 1)


length = len(arr)
result = binary_search(11, 0, length - 1)
if result != -1:
    print(result + 1)
else:
    print("없음")
