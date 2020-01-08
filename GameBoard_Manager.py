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
    print("**" * 100)
    print("leaving drop_rows")
    return new_game_array


