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
        room_data = file.read_file("room_data.csv")
        rooms = {}
        for room in room_data:
            rooms[room["ID"]] = maze.Room(room["ID"], room["Name"], room["Description"], 0, {"N": room["NORTH"], "S": room["SOUTH"], "E": room["EAST"], "W": room["WEST"]}, [], [])
        game_maze = maze.Maze(rooms, rooms["plantation"], None)
        player_data = file.read_file("player_data.csv")
        player = person.Player(player_data["Name"], game_maze.get_start_room(), int(player_data["HP"]), int(player_data["MaxHP"]), player_data["Damage"], player_data["Weapon"], player_data["Sus"], player_data["MaxSus"])
        self.set_player(player)

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
            options.append(f"{counter}. Go {exits[exit].get_name()}")
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
        display.print_new_line()
        display.smart_print("Exits:")
        exits = self.get_player().get_current_room().get_exits()
        for exit_key in exits:
            exit_room = exits[exit_key]
            display.smart_print(f"[{exit_key}] {exit_room.get_name()}", 2)
        display.print_new_line()
        display.smart_print("What will you choose?")
        for option in options:
            display.smart_print(option, 2)

    def choose_option(self):
        x = display.smart_input(int)
        if not(x > 0 and x <= len(self.get_player().get_current_room().get_exits())):
            self.choose_option()
        return x

    def execute_option(self, choice: int) -> None:
        current_room = self.get_player().get_current_room()
        exit_room = current_room.get_exits()[list(current_room.get_exits().keys())[choice - 1]]
        self.get_player().set_current_room(exit_room)

    def epilogue(self):
        display.screenbreak("=")
        display.smart_print("Thank you for playing Escape to Freedom!")
        display.smart_print("We hope you enjoyed the game.")