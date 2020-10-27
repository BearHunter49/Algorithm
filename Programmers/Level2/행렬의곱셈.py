def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr1_column = len(arr1[0])  # == arr2_row

    arr2_column = len(arr2[0])

    answer = list()
    for i in range(arr1_row):

        temp_list = list()
        for j in range(arr2_column):

            number = 0
            for k in range(arr1_column):
                number += arr1[i][k] * arr2[k][j]

            temp_list.append(number)

        answer.append(temp_list)

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
