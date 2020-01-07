from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from Player import Player


class DodgeGrid(GridLayout):
    def __init__(self, **kwargs):
        super(DodgeGrid, self).__init__(**kwargs)
        self.rows = 10
        self.cols = 7
        self.list = [0, 0, 0, 'P1', 0, 0, 0]
        for i in range(66):
            self.add_widget(Label(text="."))
        self.add_widget(Label(text="P1"))
        for i in range(3):
            self.add_widget(Label(text="."))
            
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.list[player1.position] = 0
        if keycode[1] == 'right':
            player1.move_right()
        elif keycode[1] == 'left':
            player1.move_left()
        self.list[player1.position] = 'P1'
        print(self.list)
  
        

# temp player to move around
player1 = Player('player 1')
