class Person:
    """
    Defines a person.

    Attributes:
    _name (str): the name of the person
    _current_room (Room): the room the person is in
    _inventory (List[item]): items that the person has
    _information (List[Dict[str, str]]): the pieces of information that the person has, can be true or false
    """
    def __init__(self, name, current_room) -> None:
        self._name = name
        self._current_room = current_room
        self._inventory = None
        self._information = None

class NPC(Person):
    """
    Defines an NPC.

    Additional attributes:
    _start_dialogue (Dialogue): the starting dialogue to be displayed
    """
    def __init__(self, name, current_room, start_dialogue) -> None:
        super().__init__(name, current_room)
        self._start_dialogue = None

class Combatter(Person):
    """
    Defines a combatter (person who can fight).

    Additional attributes:
    _hp (int): hp of combatter
    _max_hp (int): max_hp of combatter
    _damage (int): damage dealt by combatter per attack
    """
    def __init__(self, name, current_room, hp, max_hp, damage) -> None:
        super().__init__(name, current_room)
        self._hp = hp
        self._max_hp = max_hp
        self._damage = damage

class Player(Combatter):
    """
    Defines the Player.

    Additional attributes:
    _weapon (Weapon): name of weapon
    _sus (int): suspicion level of player
    _max_sus(int): maximum suspicion level of player
    """
    def __init__(self, name, current_room, hp, max_hp, damage, weapon, sus, max_sus) -> None:
        super().__init__(name, current_room, hp, max_hp, damage)
        self._weapon = weapon
        self._sus = sus
        self._max_sus = max_sus

class Boss(Combatter):
    """
    Defines the Boss

    Attributes:
        _entry_text (str): Text displayed when the player encounters the boss
        _escape_text (str): Text displayed when the player escapes from the boss
        _attack_text (str): Text displayed when the boss attacks the player
        _defeat_text (str): Text displayed when the player defeats the boss
    """
    def __init__(self, entry_text: str, escape_text: str, attack_text: str, defeat_text: str):
        super().__init__(name, current_room, hp, max_hp, damage)
        self._entry_text = entry_text
        self._escape_text = escape_text
        self._attack_text = attack_text
        self._defeat_text = defeat_text
