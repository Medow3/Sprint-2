from os import listdir
from Language_Handler import *

class Rune:
    def __init__(self, name: str):
        self.name = name
        self.element_icon_path = self.__icon_path(easy_icon=True)
        self.rune_icon_path = self.__icon_path(easy_icon=False)


    # returns the path to the icon, if one wants the explict icon, leave the second arg blank or True, else set to False
    # if you set to a bool, for the sake of readability write as: rune.get_icon_path(want_easy_icon=False). Although
    # the icons should be acsessed through the instances variables with dot operator, not this fucntion
    def __icon_path(self, easy_icon: bool = True):
        if easy_icon is True:
            icon_path = "game_files/icons/spells"
            for file in listdir(icon_path):
                if str(file) == self.name + ".png":
                    return icon_path + str(file)

        else:
            icon_path = "game_files/icons/runes"
            try:
                return icon_path + translation_dict()[self.name] + ".pmg"
            except KeyError:
                pass

        # if function doesnt find a icon with insances name we get here
        print(self.name, "does not have an accosiated icon in:", icon_path)
        return FileNotFoundError



