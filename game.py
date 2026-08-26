import person
import file
import display

class Game:
    """
    Initiates game functions and attributes.

    Attributes:
    player (person.Player): the player
    room_data (List[Room]): list of room data
    npc_data (List[NPC]): list of npc data
    items_data (List[Item]): list of item data
    enemy_data (List[Enemy]): list of enemy data
    """
    def __init__(self) -> None:
        self._player = None
        self._room_data = None
        self._npc_data = None
        self._items_data = None
        self._enemy_data = None

    def get_player(self) -> person.Player:
        return self._player

    def set_player(self, player_name: str) -> None:
        player_data = file.read_file("player_data.csv")
        #self, name, current_room, hp, max_hp, damage, weapon, sus, max_sus
        self._player = person.Player(player_name, player_data[])

    
        
    def welcome(self):
        print("Welcome to Escape to Freedom!")
        name = input("Enter your name: ")
        # self.set_player(person.Player(name))

    def setup(self):
        room_data = file.read_file("room_data.csv")

        player_data = file.read_file("player_data.csv")

        npc_data = file.read_file("npc.csv")

        items_data = file.read_file("items.csv")

        enemy_data = file.read_file("enemy data.csv")
    
    def is_gameover(self):

    def get_options(self):

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
        for exit in self.get_player().get_current_room().get_exits():
            display.smart_print(f"[{exit.keys()}] {exit.values().get_name()}", 2)


    def choose_option(self):

    def execute_option(self):

    def epilogue(self):
