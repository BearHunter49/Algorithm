test_list = [7, 0, 5, 4, 9, 3, 2, 1, 8]


def quick_sort(lst):
    length = len(lst)

    # break 문
    if length < 2:
        return lst

    else:
        pivot = lst[0]
        left_index = 1
        right_index = length - 1
        while True:
            for i in range(left_index, length):  # find bigger index
                if lst[i] >= pivot:
                    left_index = i
                    break

            for j in range(right_index, 0, -1):  # find smaller index
                if lst[j] < pivot:
                    right_index = j
                    break
            # End
            if right_index <= left_index:
                lst[0], lst[right_index] = lst[right_index], lst[0]
                break
            else:
                # Swap
                lst[left_index], lst[right_index] = lst[right_index], lst[left_index]
                left_index += 1
                right_index -= 1

        result = quick_sort(lst[:right_index]) + [lst[right_index]] + quick_sort(lst[right_index + 1:])
        return result


print(quick_sort(test_list))
