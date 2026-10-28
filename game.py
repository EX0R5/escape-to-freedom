import person
import file
import display
import maze
import item
from typing import List, Tuple


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
        self._texts = {}
        self._config = {}

    def get_player(self) -> person.Player:
        return self._player

    def get_maze(self) -> maze.Maze:
        return self._maze

    def set_player(self, player: person.Player) -> None:
        self._player = player

    def set_maze(self, maze: maze.Maze) -> None:
        self._maze = maze

    def set_texts(self, texts: dict) -> None:
        self._texts = texts

    def get_text(self, label: str) -> str:
        return self._texts[label]

    def set_config(self, config: dict) -> None:
        self._config = config

    def get_config(self, key: str) -> str:
        return self._config[key]

    def welcome(self):
        display.smart_print(self.get_text("welcome"))
        display.smart_print(self.get_text("name_prompt"))
        name = display.smart_input(str)
        self.get_player().set_name(name)

    def setup(self):
        self.set_texts(file.read_pairs("text.csv", "label", "text"))
        self.set_config(file.read_pairs("game.csv", "key", "value"))
        room_data = file.read_file("room_data.csv")
        rooms = {}
        for room in room_data:
            rooms[room["ID"]] = maze.Room(
                room["ID"], room["Name"], room["Description"], 0,
                {"N": room["NORTH"], "S": room["SOUTH"],
                 "E": room["EAST"], "W": room["WEST"]}, [], [])
        self.set_maze(
            maze.Maze(rooms, rooms[self.get_config("first_room")], None))
        enemy_data = file.read_file("enemy_data.csv")
        for enemy in enemy_data:
            if enemy["type"] == "Monster":
                self.get_maze().set_monster(person.Monster(
                    enemy["name"], rooms[enemy["room"]],
                    int(enemy["max_hp"]), int(enemy["max_hp"]),
                    int(enemy["attack"]), "placeholder entry text",
                    "placeholder escape text", "placeholder attack text",
                    "placeholder defeat text"))
                rooms[enemy["room"]].add_boss(self.get_maze().get_monster())
            else:
                rooms[enemy["room"]].add_boss(person.Boss(
                    enemy["name"], rooms[enemy["room"]],
                    int(enemy["max_hp"]), int(enemy["max_hp"]),
                    int(enemy["attack"]), "placeholder entry text",
                    "placeholder escape text", "placeholder attack text",
                    "placeholder defeat text"))
        player_data = file.read_file("player_data.csv")
        player = person.Player(
            player_data["Name"], self.get_maze().get_start_room(),
            int(player_data["HP"]), int(player_data["MaxHP"]),
            int(player_data["Damage"]), player_data["Weapon"],
            player_data["Sus"], player_data["MaxSus"])
        self.set_player(player)
        item_data = file.read_file("items.csv")
        for item_entry in item_data:
            # id,item_name,type,effect,value,room
            if item_entry["type"] == "Weapon":
                rooms[item_entry["room"]] = item.Weapon(
                    item_entry["item_name"], None, item_entry["value"])
            elif item_entry["type"] == "Heal":
                rooms[item_entry["room"]] = item.HealthItem(
                    item_entry["item_name"], None, item_entry["value"])
            elif item_entry["type"] == "Stealth":
                rooms[item_entry["room"]] = item.StealthItem(
                    item_entry["item_name"], None)

    def is_gameover(self):
        if self.get_player().get_sus() >= self.get_player().get_max_sus():
            display.smart_print(self.get_text("caught"))
            return True
        elif self.get_player().get_hp() <= 0:
            display.smart_print(self.get_text("died"))
            return True
        elif (self.get_player().get_current_room().get_id() ==
                self.get_config("victory_room")):
            display.print_room_title(
                self.get_player().get_current_room().get_name())
            display.smart_print(
                self.get_player().get_current_room().get_description(), 2)
            display.smart_print(self.get_text("escaped"))
            return True
        else:
            return False

    def get_options(self) -> Tuple[List[str], bool, bool]:
        """Returns: list of options, whether combat is active,
        whether monster is present"""
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
                if boss.is_monster():
                    monster_present = True
        for item in self.get_player().get_inventory():
            options.append(f"{counter}. Use {item.get_name()}")
            counter += 1
        if not monster_present:
            exits = self.get_player().get_current_room().get_exits()
            for exit in exits:
                options.append(
                    f"{counter}. Flee to {exits[exit].get_name()} [{exit}]")
                counter += 1
        return (options, combat_active, monster_present)

    def display_options(self, options: List[str], combat_active: bool,
                        monster_present: bool, skip_intro: bool) -> None:
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
            display.print_room_title(current_room.get_name())
            # check for npcs and bosses
            display.smart_print(current_room.get_description(), 2)
            display.print_new_line()
            if combat_active:
                display.print_boss_entries(current_room.get_bosses())
                display.print_combat_status(
                    current_room.get_bosses(),
                    self.get_player().get_name(),
                    self.get_player().get_hp())
            if not monster_present:
                display.print_exits(
                    self.get_text("exits_header"),
                    current_room.get_exits())
        display.print_menu(self.get_text("choose_prompt"), options)

    def choose_option(self, max_no: int) -> int:
        x = display.smart_input(int)
        if not (x > 0 and x <= max_no):
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
            display.print_attack(self.get_player().get_weapon(),
                                 self.get_player().get_damage())
            for boss in self.get_player().get_current_room().get_bosses():
                display.print_boss_attack(boss_wanted.get_name(),
                                          boss_wanted.get_damage())
                self.get_player().inc_hp(-1 * self.get_player().get_damage())
            display.print_new_line()
            display.print_combat_status(
                self.get_player().get_current_room().get_bosses(),
                self.get_player().get_name(),
                self.get_player().get_hp())
            return True
        print(self.get_text("not_implemented"))

    def epilogue(self):
        display.screenbreak("=")
        display.smart_print(self.get_text("epilogue_1"))
        display.smart_print(self.get_text("epilogue_2"))
