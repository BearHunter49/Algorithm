answer = [0, 0]


def solution(arr):
    global answer

    size = len(arr)
    my_function(arr, 0, 0, size)

    return answer


def my_function(arr, x, y, length):
    global answer
    pivot = arr[x][y]

    can_zip = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            if arr[i][j] != pivot:
                can_zip = False
                break
        if not can_zip:
            break

    if not can_zip:  # 압축 불가
        next_length = length // 2
        my_function(arr, x, y, next_length)
        my_function(arr, x + next_length, y, next_length)
        my_function(arr, x, y + next_length, next_length)
        my_function(arr, x + next_length, y + next_length, next_length)

    else:  # 압축 가능
        answer[pivot] += 1


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
