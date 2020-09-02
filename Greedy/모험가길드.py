N = int(input())  # 모험가 명 수
fears = list(map(int, input().split()))

fears.sort()  # 오름차순으로 정렬

count = 0
gathered_people = 0
for fear in fears:
    gathered_people += 1  # 본인 포함 시키기

    if fear == gathered_people:  # 인원 다 모였으면
        count += 1
        gathered_people = 0  # 모인 사람 초기화

print(count)









