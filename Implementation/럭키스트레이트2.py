N = list(map(int, input()))  # 점수

length = len(N)
mid = length // 2

pre_score = N[:mid]
post_score = N[mid:]

if sum(pre_score) == sum(post_score):
    print("LUCKY")
else:
    print("READY")





