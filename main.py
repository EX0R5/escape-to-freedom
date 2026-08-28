"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game


if __name__ == "__main__":
    mud = game.Game()
    mud.setup()
    mud.welcome()
    skip_intro = False
    while not mud.is_gameover():
        choices, combat_active, monster_present = mud.get_options()  # retrieve options as List[str]
        mud.display_options(choices, combat_active, monster_present, skip_intro)  # display
        decision = mud.choose_option(len(choices))  # get them to choose
        mud.execute_option(decision, choices)  # execute given the str version of choice
    mud.epilogue()
    
