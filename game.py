import person

class Game:
    """
    Initiates game functions and attributes.

    Attributes:
    player (person.Player): the player
    """
    def __init__(self) -> None:
        self._player = None

    def get_player(self) -> person.Player:
        return self._player

    def set_player(self, player: person.Player) -> None:
        self._player = player
        
    def welcome(self):
        print("Welcome to Escape to Freedom!")
        name = input("Enter your name: ")
        # make a player

    def setup(self):
    
    def is_gameover(self):

    def get_options(self):

    def display_options(self):

    def choose_option(self):

    def execute_option(self):

    def epilogue(self):
