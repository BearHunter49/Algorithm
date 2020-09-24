S = input()  # 문자열

consequence_count = [0, 0]
standard = ""
for c in S:
    if standard != c:  # 문자 바뀌면 기록
        consequence_count[int(c)] += 1
        standard = c

print(min(consequence_count))




