default opponent_image = None
default a = None
init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState

screen boxing_battle(player_statistics, opponent_statistics):
    # ...
    use boxing_battle_opponent(opponent_statistics)

screen boxing_battle_opponent(opponent_statistics):
    $ SetVariable("opponent_image", opponent_statistics.image)

    add opponent_image
    timer opponent_statistics.random_thinking_time repeat True action [
            SetVariable("a", opponent_statistics.update_move),
            SetVariable("opponent_image", opponent_statistics.image),
        ]
    # if opponent_statistics.current_state == FightingState.ATTACK:
    #     timer opponent_statistics.random_time_between_hits repeat opponent_statistics.current_state == FightingState.AttackMove action [
    #             Function(opponent_statistics.add_hit),
    #         ]
