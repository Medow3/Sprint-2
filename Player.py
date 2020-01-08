from Spell import Spell
from Rune import Rune


class Player:

    # position features are assuming a 7 wide playing space (this can be overridden, hopefully we eventually have this
    # as a needed parameter or a constant), thus 4 is the center. Again feel free to change.
    # don't know what the plan is with position here, feel free to move this code around all you want.
    def __init__(self, name: str, game_width: int = 7):
        self.position = round(game_width / 2)
        self.__max_position = self.position + int(game_width / 2)
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

    def cast_spell_list(self):
        self.current_spell_list = []

    def move_right(self):
        self.position += 1
        if self.position > self.__max_position:
            self.position = self.__max_position

    def move_left(self):
        self.position -= 1
        if self.position < self.__min_position:
            self.position = self.__min_position
    
    # input the other object (needs a position attribute) and returns
    # whether it and the player is colliding
    def hit_detection(self, bottom_row):
        index = 0
        for cell in bottom_row:
            if cell == "H":
                if self.position == index:
                    self.is_hit()
            index += 1

    def is_hit(self, damage):
        self.health -= damage
        

    # possibily should have a cast_current_spell_list function to this class, atlthough that may be handled best at the
    # Game class level. Depends on how you implement it with kivy integration.
