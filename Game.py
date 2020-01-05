import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from Player import Player
# from GameGrid import GameGrid



class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        
        self.cols = 1
        
        self.add_widget(Label(text='Nexus'))
        
        self.inside = GridLayout()
        self.inside.cols = 3
        self.inside.rows = 4
        
        self.one = Button(text='rune 1')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 2')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 3')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 4')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 5')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 6')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 7')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 8')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 9')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 10')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 11')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.one = Button(text='rune 12')
        self.one.bind(on_press=self.pressed)
        self.inside.add_widget(self.one)
        
        self.add_widget(self.inside)
    
    def pressed(self, instance):
        player1.add_rune_to_spell(instance)
        print('pressed', instance)



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
