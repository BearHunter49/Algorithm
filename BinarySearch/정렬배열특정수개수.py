from bisect import bisect_left, bisect_right

N, x = map(int, input().split())  # N: 원소 개수, x: 찾는 수
num_list = list(map(int, input().split()))

left_index = bisect_left(num_list, x)
right_index = bisect_right(num_list, x)

answer = right_index - left_index
if answer == 0:
    print(-1)
else:
    print(answer)



