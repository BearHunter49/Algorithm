N = int(input())
move_list = list(input().split())

move_dict = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

current_location = (1, 1)
for move in move_list:
    moving = move_dict[move]
    next_x = current_location[0] + moving[0]
    next_y = current_location[1] + moving[1]

    if next_x < 1 or next_x > N or next_y < 1 or next_y > N:  # 범위 초과하는 경우
        continue

    current_location = (next_x, next_y)

print(current_location[0], current_location[1])


