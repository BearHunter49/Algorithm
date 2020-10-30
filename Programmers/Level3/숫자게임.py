def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)
    length = len(A)

    a_index = 0
    for i in range(length):
        b = B[i]
        for j in range(a_index, length):
            if A[j] < b:
                answer += 1
                a_index = j + 1
                break
        else:
            break

    return answer


print(solution([5,1,3,7], [2,2,6,8]))

