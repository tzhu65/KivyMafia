"""
Lobby widget
"""

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class Lobby(Widget):
    house = ObjectProperty(None)
    leave = ObjectProperty(None)
    start = ObjectProperty(None)
    user_list = ObjectProperty(None)


class House(Widget):
    pass


class UserList(Widget):
    pass