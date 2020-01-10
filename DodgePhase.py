from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from Player import Player


class DodgeGrid(FloatLayout):
    def __init__(self, player: Player, **kwargs):
        super(DodgeGrid, self).__init__(**kwargs)
        self.size = (1000, 1000)
        self.player = player
        self.player_icon = Image(pos=(self.player.position * 1000, 20), size_hint=(.6, .2), source="game_files\\dirty_owl_pics\\ouwleo.png")
        self.add_widget(self.player_icon)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    # the extra variables are needed, yet unused.
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'right':
            self.player.move_right()
            self.player_icon.pos=((self.player.position/7)*300, 20)
        elif keycode[1] == 'left':
            self.player.move_left()
            self.player_icon.pos=((self.player.position/7)*300, 20)

