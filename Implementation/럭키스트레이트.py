N = input()  # 현재 점수

length = len(N)  # 점수 총 자리수
half_index = length // 2

left_score = N[:half_index]
right_score = N[half_index:]

left_sum = 0
for score in left_score:
    left_sum += int(score)

right_sum = 0
for score in right_score:
    right_sum += int(score)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")













