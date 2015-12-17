"""
Entry point for the application
"""

from kivy.app import App
from kivy.lang import Builder
from screens import AppScreenManager

# Load dependencies first
Builder.load_file('kivy/generic.kv')

Builder.load_file('kivy/create_lobby.kv')
Builder.load_file('kivy/game.kv')
Builder.load_file('kivy/lobby.kv')
Builder.load_file('kivy/lobby_list.kv')
Builder.load_file('kivy/main_menu.kv')
Builder.load_file('kivy/role_setup.kv')
Builder.load_file('kivy/settings.kv')
Builder.load_file('kivy/startup.kv')

Builder.load_file('kivy/screens.kv')


class MafiaApp(App):
    """
    Main application
    """
    def build(self):
        """
        :return: The root widget
        """
        return AppScreenManager()

if __name__ == '__main__':
    MafiaApp().run()