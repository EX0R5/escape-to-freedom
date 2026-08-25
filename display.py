import math

SCREEN_WIDTH = 60

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

def screenbreak(c: char) -> None:
    """
    Prints a screenbreak.

    Attributes:
    c (char): character to be used for screenbreak
    """
    print(SCREEN_WIDTH * c)
