from Rune import Rune


class Spell:
    def __init__(self, owner, runes: list = None):
        if runes is not None:
            self.runes = runes
        else:
            self.runes = []
        self.owner = owner

    def __repr__(self):
        string = ""
        for rune in self.runes:
            string += rune.name + " "
        return string

    # adds a rune to the spell. should only be used in the context of the players current spell
    def add_rune(self, rune: Rune):
        self.runes.append(rune)

    # casts that bad boy. This is very incomplete as I am unsure of intended behavior. Feel free to add target as a
    # parameter if needed
    def cast(self):
        row = ['.', '.', '.', '.', '.', '.', '.']
        for rune in self.runes:
            if rune.name == 'aether':
                row[0] = 'S'
            elif rune.name == 'air':
                row[1] = 'S'
            elif rune.name == 'chaos':
                row[2] = 'S'
            elif rune.name == 'earth':
                row[3] = 'S'
            elif rune.name == 'fire':
                row[4] = 'S'
            elif rune.name == 'life':
                row[5] = 'S'
            elif rune.name == 'light':
                row[6] = 'S'
            elif rune.name == 'nature':
                row[0] = 'S'
            elif rune.name == 'order':
                row[1] = 'S'
            elif rune.name == 'spirit':
                row[2] = 'S'
            elif rune.name == 'time':
                row[3] = 'S'
            elif rune.name == 'water':
                row[4] = 'S'
        return row

        # rune_names = ""
        # for rune in self.runes:
        # rune_names += rune.name + " "
        # print("casted a spell with: " + rune_names)
        # not sure what behavior to add here. Let me know whats wanted. If we are going with a gridlike dodge phase
        # where the spell approaches top down, we should probably have an external file containing a 2d-array with
        # the spell mask for each spell. eg [[0,1,0],[0,1,0],[0,1,0]] would be a 3 long line straight down the middle of
        # the screen
