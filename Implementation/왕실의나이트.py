column_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
}
knight_move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

location = input()

column = column_dict[location[0]]
row = int(location[1])

possible_move = 0
for moving in knight_move:
    n_row = row + moving[0]
    n_column = column + moving[1]

    if 1 <= n_row <= 8 and 1 <= n_column <= 8:
        possible_move += 1

print(possible_move)


