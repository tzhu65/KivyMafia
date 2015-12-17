"""
Creating a lobby
"""

from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.widget import Widget

class CreateLobby(Widget):
    lobby_name_input = StringProperty(None)
    privacy = BooleanProperty(None)
    lobby_password = StringProperty(None)
    role_setup_btn = ObjectProperty(None)