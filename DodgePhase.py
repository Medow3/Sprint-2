from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class DodgeGrid(GridLayout):
    def __init__(self, **kwargs):
        super(DodgeGrid, self).__init__(**kwargs)
        self.rows = 1
        self.cols = 1
        self.add_widget(Label(text="we get there"))
