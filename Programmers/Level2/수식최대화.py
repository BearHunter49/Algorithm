import re
from collections import deque
from itertools import permutations


def my_operate(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    else:
        return x * y


def calculate_expression(expression, possible):
    order = dict()
    for i, operator in enumerate(possible):
        order[operator] = i

    number_stack = list()
    operator_stack = list()

    for now in expression:
        if isinstance(now, int):  # 숫자
            number_stack.append(now)
            continue

        # 연산자
        if not operator_stack:  # 빈 스택
            operator_stack.append(now)
            continue

        # 스택에 존재
        if order[now] < order[operator_stack[-1]]:  # 우선순위 더 높음
            operator_stack.append(now)
        else:  # 우선순위 같거나 낮음
            while True:
                number2 = number_stack.pop()
                number1 = number_stack.pop()
                operator = operator_stack.pop()

                result = my_operate(number1, number2, operator)
                number_stack.append(result)

                if not operator_stack or order[now] < order[operator_stack[-1]]:
                    operator_stack.append(now)
                    break

    # 마지막
    number2 = number_stack.pop()
    number1 = number_stack.pop()
    operator = operator_stack.pop()

    return abs(my_operate(number1, number2, operator))


def solution(expression):
    answer = 0

    numbers = list(map(int, re.split(r'[-+*]', expression)))
    operators = re.findall(r'[-+*]', expression)

    queue = deque([])
    length = len(numbers)

    for i in range(length - 1):
        queue.append(numbers[i])
        queue.append(operators[i])
    queue.append(numbers[length - 1])

    operator_list = ["+", "-", "*"]
    possibles = list(permutations(operator_list, 3))
    for possible in possibles:
        answer = max(answer, calculate_expression(queue, possible))

    return answer


print(solution("100-200*300-500+20"))  # 60420
