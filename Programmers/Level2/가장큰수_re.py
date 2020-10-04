def my_compare(a, b):
    case1 = int(a + b)
    case2 = int(b + a)

    if case1 > case2:
        return 1
    else:
        return -1


def my_quick_sort(numbers):
    if not numbers:  # break 문
        return ''

    pivot = numbers[0]
    smaller = list()
    bigger = list()
    for number in numbers[1:]:
        if my_compare(pivot, number) == 1:  # pivot > number
            smaller.append(number)
        else:  # pivot <= number
            bigger.append(number)

    return my_quick_sort(bigger) + pivot + my_quick_sort(smaller)


def solution(numbers):
    numbers = list(map(str, numbers))
    answer = str(int(my_quick_sort(numbers)))

    return answer


# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([40,400]))
# print(solution([40,404]))
print(solution([12,121]))
# print(solution([3054,305]))
# print(solution([3044,304]))
# print(solution([340,3403]))
# print(solution([340,3402]))
# print(solution([340,3405]))
# print(solution([40,405]))
# print(solution([40,404]))
# print(solution([40,403]))
# print(solution([40,405]))
# print(solution([40,404]))
# print(solution([50,403]))
# print(solution([50,405]))
# print(solution([50,404]))
# print(solution([30,403]))
# print(solution([30,405]))
# print(solution([30,404]))
# print(solution([12,121]))
# print(solution([2,22,223]))
# print(solution([41,415]))
# print(solution([2,22 ]))
# print(solution([70,0,0,0]))
# print(solution([0,0,0,1000]))
# print(solution([0,0,0,0]))
# print(solution([0,0,70]))
# print(solution([12,1213]))
# print(solution([3, 30, 34, 5, 91]))
# print(solution([3, 30, 34, 5, 191]))
# print(solution([3, 30, 34, 5, 191, 432789]))
# print(solution([1,2,3,4,5,44]))
# print(solution([1,2,3,4,5,66]))
# print(solution([3, 30, 31, 5, 9]))
# print(solution([3, 30, 31, 34, 5, 9]))
# print(solution([3, 30, 31, 34, 33, 5, 9]))
# print(solution([10, 101]))
# print(solution([1, 11, 111, 1111]))
# print(solution([0, 0, 0, 0, 0, 0]))