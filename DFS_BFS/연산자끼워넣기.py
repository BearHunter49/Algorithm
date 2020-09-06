from itertools import permutations

N = int(input())  # 수 개수
numbers = list(map(int, input().split()))
operator_number = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈

operators = list()
for _ in range(operator_number[0]):
    operators.append("+")  # 덧셈
for _ in range(operator_number[1]):
    operators.append("-")  # 뺄셈
for _ in range(operator_number[2]):
    operators.append("*")  # 곱셈
for _ in range(operator_number[3]):
    operators.append("/")  # 나눗셈

possibles = set(permutations(operators, len(operators)))

max_num = -int(1e9)
min_num = int(1e9)
for possible in possibles:  # 모든 가능성

    total = numbers[0]
    for i in range(N - 1):

        if possible[i] == "+":  # 덧셈
            total += numbers[i + 1]
        elif possible[i] == "-":  # 뺄셈
            total -= numbers[i + 1]
        elif possible[i] == "*":  # 곱셈
            total *= numbers[i + 1]
        elif possible[i] == "/":  # 나눗셈
            total = int(total / numbers[i + 1])

    max_num = max(max_num, total)
    min_num = min(min_num, total)

print(max_num)
print(min_num)








