import math

SCREEN_WIDTH = 100

def smart_print(s: str, indent: int=0) -> None:
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
