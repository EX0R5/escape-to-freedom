import maze
import item
import dialogue

INVENTORY_SIZE = 5

class Person:
    """
    Defines a person.

    Attributes:
    _name (str): the name of the person
    _current_room (Room): the room the person is in
    _inventory (List[item]): items that the person has
    _inventory_size (int): the maximum number of items the person can carry
    _information (List[Dict[str, str]]): the pieces of information that the person has, can be true or false
    """
    def __init__(self, name: str, current_room: maze.Room) -> None:
        self._name = name
        self._current_room = current_room
        self._inventory = []
        self._information = []

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_current_room(self) -> maze.Room:
        return self._current_room

    def set_current_room(self, current_room: maze.Room) -> None:
        self._current_room = current_room

    def get_inventory(self) -> List[item.Item]:
        return self._inventory

    def append_inventory(self, item: item.Item) -> None:
        if len(self._inventory) < INVENTORY_SIZE:
            self._inventory.append(item)

    def get_information(self) -> List[Dict[str, str]]:
        return self._information

    def append_information(self, information: Dict[str, str]) -> None:
        self._information.append(information)

class NPC(Person):
    """
    Defines an NPC.

    Additional attributes:
    _start_dialogue (Dialogue): the starting dialogue to be displayed
    """
    def __init__(self, name: str, current_room: maze.Room, start_dialogue: dialogue.Dialogue = None) -> None:
        super().__init__(name, current_room)
        self._start_dialogue = start_dialogue

    def get_start_dialogue(self) -> dialogue.Dialogue:
        return self._start_dialogue

    def set_start_dialogue(self, start_dialogue: dialogue.Dialogue) -> None:
        self._start_dialogue = start_dialogue

class Combatter(Person):
    """
    Defines a combatter (person who can fight).

    Additional attributes:
    _hp (int): hp of combatter
    _max_hp (int): max_hp of combatter
    _damage (int): damage dealt by combatter per attack
    """
    def __init__(self, name: str, current_room: maze.Room, hp: int, max_hp: int, damage: int) -> None:
        super().__init__(name, current_room)
        self._hp = hp
        self._max_hp = max_hp
        self._damage = damage

    def get_hp(self) -> int:
        return self._hp

    def inc_hp(self, hp: int) -> None:
        self._hp += hp

    def get_max_hp(self) -> int:
        return self._max_hp

    def get_damage(self) -> int:
        return self._damage

    def set_damage(self, damage: int) -> None:
        self._damage = damage

class Player(Combatter):
    """
    Defines the Player.

    Additional attributes:
    _weapon (Weapon): name of weapon
    _sus (int): suspicion level of player
    _max_sus(int): maximum suspicion level of player
    """
    def __init__(self, name: str, current_room: maze.Room, hp: int, max_hp: int, damage: int, weapon: item.Weapon, sus: int, max_sus: int) -> None:
        super().__init__(name, current_room, hp, max_hp, damage)
        self._weapon = weapon
        self._sus = sus
        self._max_sus = max_sus

    def get_weapon(self) -> item.Weapon:
        return self._weapon

    def set_weapon(self, weapon: item.Weapon) -> None:
        self._weapon = weapon

    def get_sus(self) -> int:
        return self._sus

    def inc_sus(self, sus: int) -> None:
        self._sus += sus

    def get_max_sus(self) -> int:
        return self._max_sus

class Boss(Combatter):
    """
    Defines the Boss

    Attributes:
    _entry_text (str): Text displayed when the player encounters the boss
    _escape_text (str): Text displayed when the player escapes from the boss
    _attack_text (str): Text displayed when the boss attacks the player
    _defeat_text (str): Text displayed when the player defeats the boss
    """
    def __init__(self, name: str, current_room: maze.Room, hp: int, max_hp: int, damage: int, entry_text: str, escape_text: str, attack_text: str, defeat_text: str):
        super().__init__(name, current_room, hp, max_hp, damage)
        self._entry_text = entry_text
        self._escape_text = escape_text
        self._attack_text = attack_text
        self._defeat_text = defeat_text

    def get_entry_text(self) -> str:
        return self._entry_text

    def get_escape_text(self) -> str:
        return self._escape_text

    def get_attack_text(self) -> str:
        return self._attack_text

    def get_defeat_text(self) -> str:
        return self._defeat_text

class Monster(Boss):
    """
    Defines a Monster (final Boss).
    
    Additional attributes: None
    """
