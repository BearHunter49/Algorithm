import sys

N = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
req_parts = list(map(int, sys.stdin.readline().rstrip().split()))


for part in req_parts:
    if part in parts:
        print("yes", end=' ')
    else:
        print("no", end=' ')


