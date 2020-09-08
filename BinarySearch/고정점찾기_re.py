N = int(input())
num_list = list(map(int, input().split()))


def search_index_same_value(arr, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if mid == arr[mid]:
        print(mid)
        return True
    elif arr[mid] >= mid:  # 값이 인덱스보다 크면 오른쪽은 볼 필요 없음
        return search_index_same_value(arr, start, mid - 1)
    else:  # 값이 인덱스보다 작으면 왼쪽은 볼 필요 없음
        return search_index_same_value(arr, mid + 1, end)


answer = search_index_same_value(num_list, 0, N - 1)
if answer == False:
    print(-1)

# 중복 없는 경우
# 한 칸당 1씩 무조건 증/감


