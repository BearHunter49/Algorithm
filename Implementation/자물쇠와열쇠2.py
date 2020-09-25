def rotate_right(key):
    key_size = len(key)
    rotated_key = [[0] * key_size for _ in range(key_size)]

    for i in range(key_size):
        for j in range(key_size):
            rotated_key[j][(key_size - 1) - i] = key[i][j]

    return rotated_key


def check_answer(new_lock):
    lock_size = len(new_lock) // 3

    for i in range(lock_size):
        for j in range(lock_size):
            if new_lock[lock_size + i][lock_size + j] != 1:  # 하나라도 1 아니면 실패
                return False
    return True


def solution(key, lock):
    answer = False
    lock_size = len(lock)
    key_size = len(key)

    new_lock = [[0] * (lock_size * 3) for _ in range(lock_size * 3)]  # 3배 크기 새로운 자물쇠
    new_lock_size = lock_size * 3
    # lock 넣기
    for i in range(lock_size):
        for j in range(lock_size):
            new_lock[lock_size + i][lock_size + j] = lock[i][j]

    for _ in range(4):  # 회전 4가지
        key = rotate_right(key)

        for i in range(new_lock_size - key_size + 1):
            for j in range(new_lock_size - key_size + 1):

                # new_lock 에 key 넣기
                for k_i in range(key_size):
                    for k_j in range(key_size):
                        new_lock[i + k_i][j + k_j] += key[k_i][k_j]

                if check_answer(new_lock):  # 풀림
                    answer = True
                    return answer

                # key 다시 빼기
                for k_i in range(key_size):
                    for k_j in range(key_size):
                        new_lock[i + k_i][j + k_j] -= key[k_i][k_j]

    return answer


print(solution([[1, 0], [0, 0]], [[0, 1], [1, 1]]))












