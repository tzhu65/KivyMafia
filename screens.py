"""
The basic widgets that handle the different screens that the mafia app uses. All of the screens defined here are also
defined in the screens.kv file.
"""

from kivy.properties import ObjectProperty

from kivy.uix.screenmanager import ScreenManager, Screen

# imports are needed to initialize these widget classes
from startup import Startup
from main_menu import MainMenu
from settings import Settings
from create_lobby import CreateLobby
from role_setup import RoleSetup
from lobby_list import LobbyList
from lobby import Lobby
from game import Game

# Note that all object properties are defined in the screens.kv file


class AppScreenManager(ScreenManager):
    """
    Root widget that holds the different screens and handles transitioning. All the screens are passed in inside the
    screens.kv file.
    """
    startup = ObjectProperty(None)
    main_menu = ObjectProperty(None)
    settings = ObjectProperty(None)
    create_lobby = ObjectProperty(None)
    role_setup = ObjectProperty(None)
    lobby_list = ObjectProperty(None)
    lobby = ObjectProperty(None)
    game = ObjectProperty(None)


class StartupScreen(Screen):
    """
    Loading animation screen when the app first starts
    """
    startup = ObjectProperty(None)


class MainMenuScreen(Screen):
    """
    Landing screen that the application opens to
    """
    main_menu = ObjectProperty(None)


class SettingsScreen(Screen):
    """
    Panel to configure any settings
    """
    settings = ObjectProperty(None)


class CreateLobbyScreen(Screen):
    """
    Set up a new game lobby with customized game settings
    """
    create_lobby = ObjectProperty(None)

class RoleSetupScreen(Screen):
    """
    The game setup for a new lobby
    """
    role_setup = ObjectProperty(None)


class LobbyListScreen(Screen):
    """
    List of lobbies to join
    """
    lobby_list = ObjectProperty(None)


class LobbyScreen(Screen):
    """
    Waiting screen after joining a lobby
    """
    lobby = ObjectProperty(None)


class GameScreen(Screen):
    """
    Game screen
    """
    game = ObjectProperty(None)