"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game


if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    mud.add_player()
    while not mud.is_gameover():
        choices = mud.get_options()
        decision = mud.choose_option()
        mud.execute(decision)
    mud.epilogue()
    
