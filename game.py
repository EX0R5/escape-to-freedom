import person
import file
import display
import maze

FIRST_ROOM = "plantation"
MONSTER_ROOM = "final_port"
VICTORY_ROOM = "northern_sanctuary"

class Game:
    """
    Initiates game functions and attributes.

    Attributes:
    player (person.Player): the player
    maze (maze.Maze): the maze of rooms
    """
    def __init__(self) -> None:
        self._player = None
        self._maze = None

    def get_player(self) -> person.Player:
        return self._player

    def get_maze(self) -> maze.Maze:
        return self._maze

    def set_player(self, player: person.Player) -> None:
        self._player = player

    def set_maze(self, maze: maze.Maze) -> None:
        self._maze = maze
        
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
        self.set_maze(maze.Maze(rooms, rooms[FIRST_ROOM], None))
        enemy_data = file.read_file("enemy_data.csv")
        for enemy in enemy_data:
            if enemy["type"] == "Monster":
                self.get_maze().set_monster(person.Monster(enemy["name"], rooms[enemy["room"]], int(enemy["max_hp"]), int(enemy["max_hp"]), int(enemy["attack"]), "placeholder entry text", "placeholder escape text", "placeholder attack text", "placeholder defeat text"))
                rooms[enemy["room"]].add_boss(self.get_maze().get_monster())
            else:
                rooms[enemy["room"]].add_boss(person.Boss(enemy["name"], rooms[enemy["room"]], int(enemy["max_hp"]), int(enemy["max_hp"]), int(enemy["attack"]), "placeholder entry text", "placeholder escape text", "placeholder attack text", "placeholder defeat text"))
        player_data = file.read_file("player_data.csv")
        player = person.Player(player_data["Name"], self.get_maze().get_start_room(), int(player_data["HP"]), int(player_data["MaxHP"]), int(player_data["Damage"]), player_data["Weapon"], player_data["Sus"], player_data["MaxSus"])
        self.set_player(player)

    def is_gameover(self):
        if self.get_player().get_sus() >= self.get_player().get_max_sus():
            display.smart_print("You have been caught! Game over.")
            return True
        elif self.get_player().get_hp() <= 0:
            display.smart_print("You have died! Game over.")
            return True
        elif self.get_player().get_current_room().get_id() == VICTORY_ROOM:
            display.screenbreak("=")
            display.smart_print(self.get_player().get_current_room().get_name())
            display.screenbreak("=")
            display.smart_print(self.get_player().get_current_room().get_description(), 2)
            display.smart_print("You have escaped! Congratulations!")
            return True
        else:
            return False

    def get_options(self) -> Tuple(List[str], bool, bool):
        """Returns: list of options, whether combat is active, whether monster is present"""
        current_room = self.get_player().get_current_room()
        options = []
        counter = 1
        combat_active = False
        monster_present = False
        if current_room.get_bosses() != []:
            combat_active = True
            for boss in current_room.get_bosses():
                options.append(f"{counter}. Attack {boss.get_name()}")
                counter += 1
                if type(boss) == person.Monster:
                    monster_present = True
        for item in self.get_player().get_inventory():
            options.append(f"{counter}. Use {item.get_name()}")
            counter += 1
        if not monster_present:
            exits = self.get_player().get_current_room().get_exits()
            for exit in exits:
                options.append(f"{counter}. Flee to {exits[exit].get_name()} [{exit}]")
                counter += 1
        return (options, combat_active, monster_present)

    def display_options(self, options: List[str], combat_active: bool, monster_present: bool, skip_intro: bool) -> None:
        """
        Displays the options to the player.

        Attributes:
        options (List[str]): list of options to display
        combat_active (bool): if combat is active
        monster_present (bool): if monster is present
        skip_intro (bool): if the descriptions should be skipped
        """
        if not skip_intro:
            current_room = self.get_player().get_current_room()
            display.screenbreak("=")
            display.smart_print(current_room.get_name())
            display.screenbreak("=")
            # check for npcs and bosses
            display.smart_print(current_room.get_description(), 2)
            display.print_new_line()
            if combat_active:
                for boss in current_room.get_bosses():
                    display.smart_print(boss.get_entry_text(), 2)
                display.print_new_line()
                for boss in current_room.get_bosses():
                    display.smart_print(f"{boss.get_name()}: {boss.get_hp()}")
                display.smart_print(f"{self.get_player().get_name()}: {self.get_player().get_hp()}")
            if not monster_present:
                display.smart_print("Exits:")
                exits = current_room.get_exits()
                for exit_key in exits:
                    exit_room = exits[exit_key]
                    display.smart_print(f"[{exit_key}] {exit_room.get_name()}", 2)
        display.print_new_line()
        display.smart_print("What will you choose?")
        for option in options:
            display.smart_print(option, 2)

    def choose_option(self, max_no: int) -> int:
        x = display.smart_input(int)
        if not(x > 0 and x <= max_no):
            self.choose_option(max_no)
        return x

    def execute_option(self, decision: int, choices: List[str]) -> bool:
        """Returns bool if intro should be skipped"""
        decision -= 1
        if choices[decision][-1] == "]":  # move
            current_room = self.get_player().get_current_room()
            exit_room = current_room.get_exits()[choices[decision][-2]]
            self.get_player().set_current_room(exit_room)
            return False
        if "Attack" in choices[decision]:  # attack
            boss_wanted = None
            for boss in self.get_player().get_current_room().get_bosses():
                if boss.get_name() == choices[decision][10:]:
                    boss_wanted = boss
                    break
            boss_wanted.inc_hp(-1 * self.get_player().get_damage())
            if boss_wanted.get_hp() <= 0:
                display.smart_print(f"You defeated {boss_wanted.get_name()}!")
                self.get_player().get_current_room().remove_boss(boss_wanted)
            display.screenbreak("-")
            display.smart_print(f"You use the {self.get_player().get_weapon()} for {self.get_player().get_damage()} damage.")
            for boss in self.get_player().get_current_room().get_bosses():
                display.smart_print(f"{boss_wanted.get_name()} attacks you for {boss_wanted.get_damage()} damage.")
                self.get_player().inc_hp(-1 * self.get_player().get_damage())
            display.print_new_line()
            for boss in self.get_player().get_current_room().get_bosses():
                display.smart_print(f"{boss.get_name()}: {boss.get_hp()}")
            display.smart_print(f"{self.get_player().get_name()}: {self.get_player().get_hp()}")
            return True
        print("not implemented sorry")

    def epilogue(self):
        display.screenbreak("=")
        display.smart_print("Thank you for playing Escape to Freedom!")
        display.smart_print("We hope you enjoyed the game.")