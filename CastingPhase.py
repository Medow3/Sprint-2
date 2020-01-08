from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label


# from DodgePhase import *
from Player import Player
from Rune import Rune
import Language_Handler as lh


class CastGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CastGrid, self).__init__(**kwargs)

        self.cols = 1

        progress_bar = SpellDisplay(size_hint=(None, None), size=(Window.width, Window.height * 0.05))
        self.add_widget(progress_bar)

        self.nexus = Button(text='nexus')
        # lambda dark magic is needed. Don't question it
        self.nexus.bind(on_press=lambda touch: self.nexus_pressed(progress_bar))
        self.add_widget(self.nexus)

        self.inside = GridLayout()
        self.inside.cols = 3
        self.inside.rows = 4

        # initializes the 4 by 3 grid of runes from file, this is bad because the inside.cols and inside.rows are
        # just assumed to work with this file
        for rune_name in lh.translation_dict():
            self.inside.add_widget(RuneButton(rune_name))

        self.add_widget(self.inside)

    @staticmethod
    def nexus_pressed(progress_bar):
        print('added spell:', player1.current_spell, 'to spell list')
        player1.add_spell_to_spell_list()
        progress_bar.increment()


class SpellDisplay(ProgressBar):
    def __init__(self, **kwargs):
        super(SpellDisplay, self).__init__(**kwargs)
        self.max = 2
        self.value = 0

    def increment(self):
        self.value += 1
        if self.value == self.max:
            self.value = 0
            self.max += 1
            print("casted:", player1.current_spell_list)
            player1.cast_spell_list()
            global phase
            phase = 'dodgeing'
            screen_manager.switch_to(screen_manager.screens[1])


class RuneButton(Button):
    def __init__(self, name: str, **kwargs):
        super(RuneButton, self).__init__(**kwargs)
        self.text = name
        self.bind(on_press=self.rune_pressed)

    def rune_pressed(self, instance):
        player1.add_rune_to_spell(Rune(instance.text))
        print('pressed', self.text)


class Game(App):
    def build(self):
        screen_manager.add_widget(Screen(name="cast_screen"))
        screen_manager.add_widget(Screen(name="dodge_screen"))
        screen_manager.screens[0].add_widget(CastGrid())
        screen_manager.screens[1].add_widget(DodgeGrid())
        Clock.schedule_interval(screen_manager.update, 1.0 / 10.0)
        return screen_manager





class DodgeGrid(GridLayout):
    def __init__(self, **kwargs):
        super(DodgeGrid, self).__init__(**kwargs)
            
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        list[9][player1.position] = 0
        if keycode[1] == 'right':
            player1.move_right()
        elif keycode[1] == 'left':
            player1.move_left()
        list[9][player1.position] = 'P'
    
    def print_list(self):
        print(self.list)


class ScreenManager(ScreenManager):
    def update(self, dt):
        global timer
        if phase == 'dodgeing':
            print_areana()
            
            timer += 1
            
            if timer == 10:
                player1.current_spell_list[0].cast(list)
            if timer == 100:
                screen_manager.switch_to(screen_manager.screens[0])
            
            
        
        

def print_areana():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for i in list:
        print(*i)


# please forgive the sin of the globals
list = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 'P', 0, 0, 0]]
timer = 0
screen_manager = ScreenManager()
player1 = Player('player 1')
phase = 'casting'
Game().run()
