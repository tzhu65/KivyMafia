"""
Main menu widget
"""

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class MainMenu(Widget):
    create_lobby = ObjectProperty(None)
    join_lobby = ObjectProperty(None)
    stats = ObjectProperty(None)
    settings = ObjectProperty(None)
    customize_character = ObjectProperty(None)