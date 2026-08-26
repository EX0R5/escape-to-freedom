import person
import file
import display
import maze

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
        display.smart_print("Welcome to Escape to Freedom!")
        display.smart_print("Please enter your name:")
        name = display.smart_input(str)
        self.get_player().set_name(name)

    def setup(self):
    
    def is_gameover(self):
        if self.get_player().get_sus() >= self.get_player().get_max_sus():
            display.smart_print("You have been caught! Game over.")
            return True
        elif self.get_player().get_hp() <= 0:
            display.smart_print("You have died! Game over.")
            return True
        elif self.get_player().get_current_room().get_id() == "northern_sanctuary":
            display.screenbreak("=")
            display.smart_print(self.get_player().get_current_room().get_name())
            display.screenbreak("=")
            display.smart_print(self.get_player().get_current_room().get_description(), 2)
            display.smart_print("You have escaped! Congratulations!")
            return True
        else:
            return False

    def get_options(self) -> List[str]:
        options = []
        counter = 1
        exits = self.get_player().get_current_room().get_exits()
        for exit in exits:
            options.append(f"{counter}. Go {exits[exit]}")
            counter += 1
        return options

    def display_options(self, options: List[str]) -> None:
        """
        Displays the options to the player.

        Attributes:
        options (List[str]): list of options to display
        """
        display.screenbreak("=")
        display.smart_print(self.get_player().get_current_room().get_name())
        display.screenbreak("=")
        # check for npcs and bosses
        display.smart_print(self.get_player().get_current_room().get_description(), 2)
        display.smart_print("")
        display.smart_print("Exits:")
        for option in options:
            display.smart_print(option, 2)
        display.smart_print("What will you choose?")

    def choose_option(self):
        x = display.smart_input(int)
        if not(x > 0 and x <= len(self.get_player().get_current_room().get_exits())):
            self.choose_option()
        return x

    def execute_option(self, choice: int) -> None:
        self.get_player().set_current_room(self.get_player().get_current_room().get_exits()[list(self.get_player().get_current_room().get_exits().keys())[x - 1]])

    def epilogue(self):
        display.screenbreak("=")
        display.smart_print("Thank you for playing Escape to Freedom!")
        display.smart_print("We hope you enjoyed the game.")