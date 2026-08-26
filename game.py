import person
import file
import display
import maze

class Game:
    """
    Initiates game functions and attributes.

    Attributes:
    player (person.Player): the player
    room_data (Dict[str, Room]): the maze
    maze (maze.Maze): the maze
    npc_data (List[NPC]): list of npc data
    items_data (List[Item]): list of item data
    enemy_data (List[Enemy]): list of enemy data
    """
    def __init__(self) -> None:
        self._player = None
        self._room_data = {}
        self._npc_data = []
        self._items_data = []
        self._enemy_data = []
        self._maze = None

    def get_player(self) -> person.Player:
        return self._player

    def set_player(self, player_name: str = None) -> None:
        player_data = file.read_file("player_data.csv")[0]
        self._player = person.Player(player_name, self.get_room_data()[player_data["CurrentRoom"]], int(player_data["HP"]), int(player_data["MaxHP"]), 1, player_data["Weapon"], int(player_data["Sus"]), int(player_data["MaxSus"]))

    def get_room_data(self) -> Dict[str, maze.Room]:
        return self._room_data

    def set_room_data(self) -> None:
        room_data = file.read_file("room_data.csv")
        for room in room_data:
            built_room = maze.Room(room["ID"], room["Name"], room["Description"], 0, {"N": room["NORTH"], "S": room["SOUTH"], "E": room["EAST"], "W": room["WEST"]}, None, None)
            self._room_data[room["ID"]] = built_room

    def get_maze(self) -> maze.Maze:
        return self._maze

    def set_maze(self, maze: maze.Maze) -> None:
        self._maze = maze.Maze(self.get_room_data(), self.get_room_data()[self.get_player().get_current_room()], None)

    # def get_npc_data(self) -> list:
    #     return self._npc_data

    # def set_npc_data(self, npc_data: list) -> None:
    #     self._npc_data = npc_data

    # def get_items_data(self) -> list:
    #     return self._items_data

    # def set_items_data(self, items_data: list) -> None:
    #     self._items_data = items_data

    # def get_enemy_data(self) -> list:
    #     return self._enemy_data

    # def set_enemy_data(self, enemy_data: list) -> None:
    #     self._enemy_data = enemy_data
        
    def welcome(self):
        display.smart_print("Welcome to Escape to Freedom!")
        display.smart_print("Please enter your name:")
        name = display.smart_input(str)
        self.get_player().set_name(name)

    def setup(self):
        self.set_room_data()
        self.set_player()

        # npc_data = file.read_file("npc.csv")

        # items_data = file.read_file("items.csv")

        # enemy_data = file.read_file("enemy data.csv")
    
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