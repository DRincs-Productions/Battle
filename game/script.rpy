# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

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
    call screen boxing_battle_opponent(opp)
    pause

    # This ends the game.

    return
