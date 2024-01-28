default opponent_image = None
default a = None
init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState

screen boxing_battle(player_statistics, opponent):
    # ...
    use boxing_battle_opponent(opponent)

screen boxing_battle_opponent(opponent):
    $ SetVariable("opponent_image", opponent.image)

    add opponent_image
    timer opponent.random_thinking_time repeat True action [
            Function(opponent.update_move),
            SetVariable("opponent_image", opponent.image),
            Function(renpy.restart_interaction),
        ]
    # if opponent.current_state == FightingState.ATTACK:
    #     timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
    #             Function(opponent.add_hit),
    #         ]
