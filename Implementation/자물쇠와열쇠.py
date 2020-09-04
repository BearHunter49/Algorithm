import copy


def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)

    # 3배 크기의 lock 생성
    expanded_lock_len = lock_len * 3
    expanded_lock = [[0] * expanded_lock_len for _ in range(expanded_lock_len)]

    # 가운데에 원래 lock 박기
    for i in range(lock_len):
        for j in range(lock_len):
            expanded_lock[lock_len + i][lock_len + j] = lock[i][j]

    # key 회전 해 가면서 확인
    for _ in range(4):
        key = rotate_90(key)

        # 확장된 lock 완전 탐색
        for i in range(2 * lock_len):
            for j in range(2 * lock_len):
                temp_lock = copy.deepcopy(expanded_lock)  # 매번 key 박은거 초기화

                # key 넣기
                for x in range(key_len):
                    for y in range(key_len):
                        temp_lock[i + x][j + y] += key[x][y]

                # key 맞는지 확인
                if check(temp_lock, lock_len) == True:
                    return True

    # 결국 맞는 key 없으면
    return False


# 자물쇠에 키 맞는지 확인
def check(arr, lock_len):
    for i in range(lock_len):
        for j in range(lock_len):
            if arr[lock_len + i][lock_len + j] != 1:  # 1이 아니면 틀림
                return False

    # 다 1이면 통과
    return True


# 90도 회전
def rotate_90(arr):
    row_len = len(arr)
    column_len = len(arr[0])
    arr2 = [[0] * row_len for _ in range(column_len)]  # 행 열 뒤집음

    # 회전
    for i in range(row_len):
        for j in range(column_len):
            arr2[j][row_len - 1 - i] = arr[i][j]

    return arr2


print(solution([[1, 0], [0, 0]], [[0, 1], [1, 1]]))

# True


