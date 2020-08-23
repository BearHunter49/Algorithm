N = int(input())

count = 0
for h in range(N + 1):
    if h == 3 or h == 13 or h == 23:
        count += 60 * 60
    else:
        count += 15 * 60 + 45 * 15

print(count)
