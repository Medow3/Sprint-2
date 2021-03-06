from Spell import Spell
from Rune import Rune

class Player:

    # position features are assuming a 7 wide playing space (this can be overridden, hopefully we evenutally have this
    # as a needed perameter or a constant), thus 4 is the center. Again feel free to change.
    # don't know what the plan is with position here, feek free to move this code around all you want.
    def __init__(self, name: str, game_width: int = 7):
        self.position = round(game_width/2)
        self.__max_position = self.position + int(game_width/2)
        self.__min_position = 0
        self.name = name
        self.health = 100
        self.current_spell = Spell(self)
        self.current_spell_list = []

    # starts the next spell on a clean slate and adds the recent spell to the spell list
    def add_spell_to_spell_list(self):
        self.current_spell_list.append(self.current_spell)
        self.current_spell = Spell(self)

    # adds runes to the current spell, this would be triggered by dragging / clicking runes
    def add_rune_to_spell(self, rune: Rune):
        self.current_spell.add_rune(rune)

    def move_right(self):
        self.position += 1
        if self.position > self.__max_position:
            self.position = self.__max_position

    def move_left(self):
        self.position -= 1
        if self.position < self.__min_position:
            self.position = self.__min_position

    # possibily should have a cast_current_spell_list function to this class, atlthough that may be handled best at the
    # Game class level. Depends on how you implement it with kivy integration.