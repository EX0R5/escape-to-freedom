import math

SCREEN_WIDTH = 100


def smart_print(s: str, indent: int = 0) -> None:
    """
    Prints, but wraps text if it overflows the screen width.

    Attributes:
    s (str): string to printed
    indent (int): any indentation needed for each line
    """
    empty_char = SCREEN_WIDTH - indent
    if len(s) <= empty_char:
        print(" " * indent + s)
        return
    temp = s[:empty_char]
    for i in range(len(temp) - 1, -1, -1):
        if temp[i] == " ":
            print(" " * indent + temp[:i])
            smart_print(s[i + 1:], indent)
            return


def screenbreak(c: str) -> None:
    """
    Prints a screenbreak.

    Attributes:
    c (char): character to be used for screenbreak
    """
    print(SCREEN_WIDTH * c)


def smart_input(type_wanted: type) -> type:
    """
    Gets input from user, but checks if it is of the correct type.

    Attributes:
    type_wanted (type): type of input expected from user

    Returns:
    the final input, converted to the correct type
    """
    while True:
        x = input("> ")
        if type_wanted == str:
            return x
        if type_wanted == int:
            if not x.isdigit():
                print("Please enter a valid number.")
                continue
            return int(x)
        print("Not implemented yet")


def print_new_line() -> None:
    """
    Prints a new line.
    """
    print(" ")


def print_room_title(name: str) -> None:
    """
    Prints the title card of a room.

    Attributes:
    name (str): name of the room
    """
    screenbreak("=")
    smart_print(name)
    screenbreak("=")


def print_boss_entries(bosses: list) -> None:
    """
    Prints the entry text of every boss in the room.

    Attributes:
    bosses (list): the bosses to introduce
    """
    for boss in bosses:
        smart_print(boss.get_entry_text(), 2)
    print_new_line()


def print_combat_status(bosses: list, player_name: str,
                        player_hp: int) -> None:
    """
    Prints the hp row of every boss and of the player.

    Attributes:
    bosses (list): the bosses fighting
    player_name (str): name of the player
    player_hp (int): hp of the player
    """
    for boss in bosses:
        smart_print(f"{boss.get_name()}: {boss.get_hp()}")
    smart_print(f"{player_name}: {player_hp}")


def print_exits(header: str, exits: dict) -> None:
    """
    Prints the header and the exits of the room.

    Attributes:
    header (str): text printed above the exits
    exits (dict): the exits of the room
    """
    smart_print(header)
    for exit_key in exits:
        exit_room = exits[exit_key]
        smart_print(f"[{exit_key}] {exit_room.get_name()}", 2)


def print_menu(prompt: str, options: list) -> None:
    """
    Prints the choice prompt and the options below it.

    Attributes:
    prompt (str): text printed above the options
    options (list): the options to print
    """
    print_new_line()
    smart_print(prompt)
    for option in options:
        smart_print(option, 2)


def print_attack(weapon: str, damage: int) -> None:
    """
    Prints the player's attack line under a screenbreak.

    Attributes:
    weapon (str): name of the weapon used
    damage (int): damage dealt by the player
    """
    screenbreak("-")
    smart_print(f"You use the {weapon} for {damage} damage.")


def print_boss_attack(name: str, damage: int) -> None:
    """
    Prints a boss's counterattack line.

    Attributes:
    name (str): name of the boss
    damage (int): damage dealt by the boss
    """
    smart_print(f"{name} attacks you for {damage} damage.")
