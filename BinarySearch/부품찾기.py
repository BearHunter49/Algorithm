import sys

N = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
req_parts = list(map(int, sys.stdin.readline().rstrip().split()))

# 정렬
parts.sort()


# 이진 탐색
def binary_search(target, start, end):
    # break 문
    if start > end:
        return False

    mid = (start + end) // 2
    if parts[mid] == target:  # find
        return True
    elif parts[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)


for part in req_parts:
    if binary_search(part, 0, N - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')



