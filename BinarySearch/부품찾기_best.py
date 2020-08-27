import sys

N = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
req_parts = list(map(int, sys.stdin.readline().rstrip().split()))

max_num = max(parts)
counting_of_parts = [0] * max_num

for part in parts:
    counting_of_parts[part] += 1

for req_part in req_parts:
    if counting_of_parts[req_part]:
        print("yes", end=' ')
    else:
        print("no", end=' ')
