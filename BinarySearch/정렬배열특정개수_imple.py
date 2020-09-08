N, x = map(int, input().split())  # N: 원소 개수, x: 찾는 수
num_list = list(map(int, input().split()))


def left_index(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target and (mid == 0 or arr[mid - 1] != target):  # 조건 맞거나 맨 앞이면 리턴
        return mid
    elif target <= arr[mid]:  # 같거나 더 작으면
        return left_index(arr, target, start, mid - 1)
    else:  # 더 크면
        return left_index(arr, target, mid + 1, end)


def right_index(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target and (mid == N - 1 or arr[mid + 1] != target):  # 조건 맞거나 맨 뒤면 리턴
        return mid
    elif target < arr[mid]:  # 더 작으면
        return right_index(arr, target, start, mid - 1)
    else:  # 같거나 더 크면
        return right_index(arr, target, mid + 1, end)


right = right_index(num_list, x, 0, N - 1)
left = left_index(num_list, x, 0, N - 1)

if right == None or left == None:
    print(-1)
else:
    answer = right - left + 1
    print(answer)



