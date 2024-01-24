﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    python:
        from pythonpackages.boxing_battle.fighting_move import DefenseMove
        from pythonpackages.boxing_battle.character_statistics import OpponentStatistics

        defense = DefenseMove(
            name = "Block",
            icon = "icon block",
            animation_image = "opponent block",
        )
        opp = OpponentStatistics(
            health = 100,
            stamina = 100,
            recovery_percentage_stamina = 0.1,
            idle_image = "opponent idle",
            damage_imaged = "opponent damage",
            defense = defense,
        )
    show screen boxing_battle_opponent(opp)

    ""

    return
