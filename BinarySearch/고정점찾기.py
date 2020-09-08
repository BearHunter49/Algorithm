N = int(input())
num_list = list(map(int, input().split()))


def search_index_same_value(arr, size, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if mid == arr[mid]:
        print(mid)
        return True
    elif arr[mid] >= size:  # 최대 인덱스보다 크면 오른쪽은 볼 필요 없음
        return search_index_same_value(arr, size, start, mid - 1)
    elif arr[mid] < 0:  # 0 보다 작으면 왼쪽은 볼 필요 없음
        return search_index_same_value(arr, size, mid + 1, end)
    else:  # 양쪽 다 보기
        left = search_index_same_value(arr, size, start, mid - 1)
        right = search_index_same_value(arr, size, mid + 1, end)
        return left or right


answer = search_index_same_value(num_list, N - 1, 0, N - 1)
if answer == False:
    print(-1)

# 중복 포함하는 경우
# 최악의 경우 O(N) 선형시간 걸림


