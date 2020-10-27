import re
from itertools import permutations
import copy


def solution(expression):
    answer = 0

    numbers = re.split(r'[-+*]', expression)
    operators = re.findall(r'[-+*]', expression)

    queue = list()
    length = len(numbers)

    for i in range(length - 1):
        queue.append(numbers[i])
        queue.append(operators[i])
    queue.append(numbers[length - 1])

    operator_list = ["+", "-", "*"]
    operators_count = dict()
    for operator in operator_list:
        operators_count[operator] = operators.count(operator)

    possibles = list(permutations(operator_list, 3))
    for possible in possibles:

        new_list = copy.deepcopy(queue)
        for operator in possible:
            for _ in range(operators_count[operator]):  # 해당 연산자 수 만큼 계산
                index = new_list.index(operator)
                result = str(eval(new_list[index - 1] + operator + new_list[index + 1]))
                new_list = new_list[:index - 1] + [result] + new_list[index + 2:]

        answer = max(answer, abs(int(new_list[0])))

    return answer


print(solution("100-200*300-500+20"))  # 60420
