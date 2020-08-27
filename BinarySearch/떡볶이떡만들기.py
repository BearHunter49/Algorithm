N, M = map(int, input().split())
dducks = list(map(int, input().split()))

max_length = max(dducks)
record = list()  # (자른 길이, 잘린 떡 길이)


def binary_dduck(start, end):
    # break 문
    if start > end:
        return

    # 중간 길이로 자르기
    mid = (start + end) // 2
    right_dducks = [i for i in dducks if i > mid]
    remain_dduck = sum(right_dducks) - (len(right_dducks) * mid)

    if remain_dduck == M:  # 딱 일치
        record.append((mid, remain_dduck))
        return
    elif remain_dduck > M:  # 더 자른 경우
        record.append((mid, remain_dduck))
        binary_dduck(mid + 1, end)
    else:  # 덜 자른 경우
        binary_dduck(start, mid - 1)


binary_dduck(0, max_length)
record.sort(key=lambda x: x[1])
print(record[0][0])
