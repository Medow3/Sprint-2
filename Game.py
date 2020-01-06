from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window

from Player import Player
from Rune import Rune
import Language_Handler as lh


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

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

        # leftover code
        # self.fire = Button(text='fire')
        # self.fire.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.fire)
        #
        # self.water = Button(text='water')
        # self.water.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.water)
        #
        # self.air = Button(text='air')
        # self.air.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.air)
        #
        # self.four = Button(text='rune 4')
        # self.four.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.four)
        #
        # self.five = Button(text='rune 5')
        # self.five.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.five)
        #
        # self.six = Button(text='rune 6')
        # self.six.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.six)
        #
        # self.seven = Button(text='rune 7')
        # self.seven.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.seven)
        #
        # self.eight = Button(text='rune 8')
        # self.eight.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.eight)
        #
        # self.nine = Button(text='rune 9')
        # self.nine.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.nine)
        #
        # self.ten = Button(text='rune 10')
        # self.ten.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.ten)
        #
        # self.eleven = Button(text='rune 11')
        # self.eleven.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.eleven)
        #
        # self.twelve = Button(text='rune 12')
        # self.twelve.bind(on_press=self.rune_pressed)
        # self.inside.add_widget(self.twelve)

        self.add_widget(self.inside)

    @staticmethod
    def nexus_pressed(progress_bar):
        progress_bar.increment()
        print('added spell:', player1.current_spell, 'to spell list')
        player1.add_spell_to_spell_list()


class SpellDisplay(ProgressBar):
    def __init__(self, **kwargs):
        super(SpellDisplay, self).__init__(**kwargs)
        self.max = 2
        self.value = 0

    def increment(self):
        if self.value == self.max:
            # TODO player1.cast()
            self.value = 0
            self.max += 1
            return
        self.value += 1


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
        return Grid()


player_list = []
player1 = Player('player 1')
player2 = Player('player 2')
player_list.append(player1)
player_list.append(player2)
Game().run()
