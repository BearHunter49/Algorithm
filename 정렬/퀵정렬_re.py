import random

test_list = [random.randint(0, 20) for i in range(20)]
print(test_list)
# test_list = [7, 0, 5, 4, 9, 3, 2, 1, 8]


def quick_sort(lst):
    length = len(lst)
    # break 문
    if length < 2:
        return lst

    pivot = lst[0]
    tail = lst[1:]  # pivot 제외
    left_lst = [x for x in tail if x < pivot]
    right_list = [x for x in tail if x >= pivot]

    return quick_sort(left_lst) + [pivot] + quick_sort(right_list)


print(quick_sort(test_list))
