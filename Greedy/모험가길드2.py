N = int(input())  # 모험가 수
fears = list(map(int, input().split()))  # 공포도

fears.sort()  # 오름차순 정렬

result = 0
gathered = 0
for fear in fears:
    gathered += 1
    if gathered == fear:  # 모인 사람 수 == 필요한 공포도
        result += 1
        gathered = 0

print(result)









