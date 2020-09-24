S = list(map(int, input()))  # 숫자 문자열

result = S[0]  # 첫번째 값으로 시작
for i in range(1, len(S)):
    if result <= 1 or S[i] <= 1:  # 1이나 0은 더하기
        result += S[i]
    else:
        result *= S[i]

print(result)







