from random import randint

# this dict is dirrived from rune_spell_dict.csv with format spell_name
def translation_dict():
    dictionary = {}
    for line in open("game_files/rune_spell_dict.csv"):
        name_image = tuple(line.split(","))
        dictionary[name_image[0]] = name_image[1]
    return dictionary

def scramble_dict_file():
    element_list = []
    rune_list = []
    for element, rune in translation_dict().items():
        element_list.append(element.replace(" ", ""))
        rune_list.append(rune.replace(" ", ""))
    with open("game_files/rune_spell_dict.csv", "w") as file:
        for element in element_list:
            new_line = element + ", " + rune_list.pop(randint(0,len(rune_list)-1))
            file.write(new_line)

