S = input()

alphabet_list = list()
sum_of_number = 0

for c in S:
    if c.isdecimal() == True:
        sum_of_number += int(c)  # 정수형으로 변환하여 저장
    else:
        alphabet_list.append(c)

alphabet_list.sort()  # 오름차순 정렬
if sum_of_number != 0:
    print(f"{''.join(alphabet_list)}{sum_of_number}")
else:
    print(f"{''.join(alphabet_list)}")



