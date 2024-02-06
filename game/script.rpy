# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    python:
        from pythonpackages.boxing_battle.fighting_move import DefenseMove, AttackMove
        from pythonpackages.boxing_battle.character_statistics import OpponentStatistics, PlayerStatistics

        defense = DefenseMove(
            name = "Block",
            icon = "icon block",
            animation_image = "opponent block",
            key = "a",
        )
        attack = AttackMove(
            name = "Punch",
            icon = "icon punch",
            animation_image = ["opponent attack_a", "opponent attack_b"],
            health_damage = 10,
            stamina_damage = 10,
            required_stamina = 10,
            key = "b",
            stum_time = 0.7,
        )
        opponent = OpponentStatistics(
            health = 100,
            stamina = 100,
            recovery_percentage_stamina = 30,
            idle_image = "opponent idle",
            damage_imaged = "opponent damage",
            defense = defense,
            attack = attack,
            minimal_time_between_hits = 0.5,
            maximal_time_between_hits = 1,
        )
        player = PlayerStatistics(
            health = 100,
            stamina = 100,
            recovery_percentage_stamina = 30,
            idle_image = "player idle",
            damage_imaged = "player damage",
            x_button = attack,
            y_button = defense,
            a_button = attack,
            b_button = defense,
            down_button = attack,
            left_button = defense,
            right_button = attack,
            up_button = defense,
        )
    $ renpy.show(player.idle_image)
    $ renpy.show(opponent.image)
    show screen boxing_player_thinking(player, opponent)
    show screen boxing_opponent_thinking(player, opponent)
    call screen boxing_battle_interface(player, opponent)

    # This ends the game.

    return
