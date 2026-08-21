"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game


if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    while not mud.is_gameover():
        choices = mud.get_options()  # retrieve options as List[str]
        mud.display_options(choices)  # display
        decision = mud.choose_option()  # get them to choose
        mud.execute_option(decision)  # execute given the str version of choice
    mud.epilogue()
    
