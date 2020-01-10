from Player import Player


def drop_rows(game_array: list, player: Player, new_row="FIXME"):
    new_game_array = game_array[:]
    index = 0
    while index < len(new_game_array) - 1:
        row1 = game_array[index]
        new_game_array[index + 1] = row1
        index += 1
    if new_row == "FIXME":
        # print("no row passed in")
        new_game_array[0] = ['.', '.', '.', '.', '.', '.', '.']
    elif new_row is None:
        # print("None row passed in")
        new_game_array[0] = ['.', '.', '.', '.', '.', '.', '.']
    else:
        # print("passed in row:", new_row)
        new_game_array[0] = new_row
    temp = new_game_array[len(new_game_array) - 1]
    # print("len:", len(temp))
    # print("pos:", player.position)
    player.hit_detection(temp)
    temp[player.position] = "P"
    # print("**" * 100)
    # print("leaving drop_rows")
    return new_game_array
