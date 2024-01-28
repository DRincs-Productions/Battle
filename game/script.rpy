# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    python:
        from pythonpackages.boxing_battle.fighting_move import DefenseMove, AttackMove
        from pythonpackages.boxing_battle.character_statistics import OpponentStatistics

        defense = DefenseMove(
            name = "Block",
            icon = "icon block",
            animation_image = "opponent block",
        )
        attack = AttackMove(
            name = "Punch",
            icon = "icon punch",
            animation_image = "opponent attack",
            health_damage = 10,
            stamina_damage = 10,
            required_stamina = 10,
        )
        opp = OpponentStatistics(
            health = 100,
            stamina = 100,
            recovery_percentage_stamina = 0.1,
            idle_image = "opponent idle",
            damage_imaged = "opponent damage",
            defense = defense,
            attack = attack,
        )
    call screen boxing_battle_opponent(opp)

    # This ends the game.

    return
