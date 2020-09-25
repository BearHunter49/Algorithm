S = input()

alpha_list = list()
total = 0
for c in S:
    if c.isdecimal():
        total += int(c)
    else:
        alpha_list.append(c)

alpha_list.sort()  # 오름차순
print(''.join(alpha_list), end='')
print(total)

# 알파벳 26개니까 counting으로 하는게 더 효율적일듯.
# 하지만 dict 만들기 귀찮으니 그냥 함
