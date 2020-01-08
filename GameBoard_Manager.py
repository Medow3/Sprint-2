from Player import Player


def drop_rows(game_array: list, player: Player, new_row=None):
    new_game_array = game_array[:]
    index = 0
    while index < len(new_game_array) - 1:
        row1 = game_array[index]
        new_game_array[index+1] = row1
        index += 1
    new_game_array[0] = new_row
    new_game_array[len(new_game_array)-1][player.position] = "p"
    for row in new_game_array:
        print(row)
    print("**" * 100)
    return new_game_array


marcus = Player("marcus")
original = [[1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, "p", 0, 0, 0]]
a = drop_rows(original, marcus, ["H", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["E", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["L", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["L", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["O", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["W", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["O", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["R", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["L", 0, 0, 0, 0, 0, 0])
a = drop_rows(a, marcus, ["D", 0, 0, 0, 0, 0, 0])


