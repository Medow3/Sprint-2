import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from Player import Player
from Rune import Rune
# from GameGrid import GameGrid



class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        
        self.cols = 1
        
        self.nexus = Button(text='nexus')
        self.nexus.bind(on_press=self.pressed)
        self.add_widget(self.nexus)
        
        self.inside = GridLayout()
        self.inside.cols = 3
        self.inside.rows = 4
        
        self.fire = Button(text='fire')
        self.fire.bind(on_press=self.pressed)
        self.inside.add_widget(self.fire)
        
        self.water = Button(text='water')
        self.water.bind(on_press=self.pressed)
        self.inside.add_widget(self.water)
        
        self.air = Button(text='air')
        self.air.bind(on_press=self.pressed)
        self.inside.add_widget(self.air)
        
        self.four = Button(text='rune 4')
        self.four.bind(on_press=self.pressed)
        self.inside.add_widget(self.four)
        
        self.five = Button(text='rune 5')
        self.five.bind(on_press=self.pressed)
        self.inside.add_widget(self.five)
        
        self.six = Button(text='rune 6')
        self.six.bind(on_press=self.pressed)
        self.inside.add_widget(self.six)
        
        self.seven = Button(text='rune 7')
        self.seven.bind(on_press=self.pressed)
        self.inside.add_widget(self.seven)
        
        self.eight = Button(text='rune 8')
        self.eight.bind(on_press=self.pressed)
        self.inside.add_widget(self.eight)
        
        self.nine = Button(text='rune 9')
        self.nine.bind(on_press=self.pressed)
        self.inside.add_widget(self.nine)
        
        self.ten = Button(text='rune 10')
        self.ten.bind(on_press=self.pressed)
        self.inside.add_widget(self.ten)
        
        self.eleven = Button(text='rune 11')
        self.eleven.bind(on_press=self.pressed)
        self.inside.add_widget(self.eleven)
        
        self.twelve = Button(text='rune 12')
        self.twelve.bind(on_press=self.pressed)
        self.inside.add_widget(self.twelve)
        
        self.add_widget(self.inside)
    
    def pressed(self, instance):
        player1.add_rune_to_spell(Rune(instance.text))
        print('pressed', instance.text)

    def nexus_pressed(self, instance):
        player1.add_spell_to_spell_list()
        print('add_spell_to_spell_list')


# I would have a large class like this to contain everything and run the game updates. 
# Again this could be a kivy class
class Game(App):
    def build(self):
        return Grid()


player_list = []
player1 = Player('player 1')
player2 = Player('player 2')
player_list.append(player1)
player_list.append(player2)
Game().run()
