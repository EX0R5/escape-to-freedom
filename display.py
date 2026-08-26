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
    for i in range(math.ceil(len(s) / empty_char)):
        print(" " * indent + s[i * empty_char : (i + 1) * empty_char])

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
